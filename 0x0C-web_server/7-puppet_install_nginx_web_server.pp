# Install and config the nginx
package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file { '/var/www/html/index.html':
  content => 'Hollo World!',
  path    => '/var/www/html/index.html'
}


