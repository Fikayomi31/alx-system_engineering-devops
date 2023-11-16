# increase the amount of traffic an Nginx can handle

exec {'replace line':
   command  => 'sed -i "s|ULIMIT=\"-n 15"|ULIMIT=\"-n 5000\"|" /etc/default/nginx',
   provider => 'shell',
}
-> exec {'restart nginx':
   command  => 'nginx restart',
   provider => 'shell',
}
