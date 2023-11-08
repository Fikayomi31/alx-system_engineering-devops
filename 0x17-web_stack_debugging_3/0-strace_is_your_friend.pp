# Fix apache2 whicb is running error 50

exec {'Fix error 500'
  command  => 'sed i "s/phpp/php/g" /var/www/html/wp-setting.php',
  provider => 'shell'
}
