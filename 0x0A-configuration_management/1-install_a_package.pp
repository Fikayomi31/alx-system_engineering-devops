# Installing flask from pip3 and version must be 2.1.0

package { 'flask':
  provider => 'pip3',
  name     => 'flask',
  ensure   => '2.1.0',
}