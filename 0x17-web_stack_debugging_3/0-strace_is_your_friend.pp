# Fix error 500 which is shelling error in a file

exec { 'replace_line':
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  provider => 'shell'
}
