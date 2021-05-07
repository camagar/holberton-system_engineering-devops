# install and configure an Nginx server using Puppet instead of Bash

package { 'nginx':
  ensure  => installed,
  name    => 'nginx',
}

file { '/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.holbertonschool.co permanent;',
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
