# kill a process
exec { 'killmenow':
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  command     => 'pkill killmenow',
}
