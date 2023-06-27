# Installing and configuring nginx server

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => present,
    content => "Hello World!\n",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => 'server {
                  listen 80 default_server;
                  listen [::]:80 default_server;
                  server_name _;

                  location = /redirect_me {
                    return 301 https://www.tcinfo.com/new-page;
                  }

                  location / {
                    root /var/www/html;
                  }
                }',
    notify => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }
}

class { 'nginx': }
