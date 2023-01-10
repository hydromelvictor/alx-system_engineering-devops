# 4. Client configuration file (w/ Puppet)

file_line{'passwd off':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line{'file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}

