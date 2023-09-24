# Puppet to make changes to our configuration file
file_line { 'Turn off passwd':
  ensure  => present,
  path    => 'etc/ssh/ssh_config',
  line    => '  PassAuthentication no',
  replace => true,
}

file_line { 'Identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '  IdentityFile ~/.ssh/school',
  replace => true,
}
