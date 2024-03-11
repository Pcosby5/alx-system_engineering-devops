# Puppet manifest to fix Apache 500 error
class apache_fix {
    package { 'apache2':
        ensure => installed,
    }
}

    file { '/etc/apache2/apache2.conf':
        ensure  => file,
        content => template('apache/apache2.conf.erb'),
        notify  => Service['apache2'],
    }


    service { 'apache2':
        ensure  => running,
        enable}
