CREATE TABLE vm (
  id  INT AUTO_INCREMENT,
  vmname  VARCHAR(255) NOT NULL,
  hostname  VARCHAR(255) DEFAULT NULL,
  ipaddress VARCHAR(255) DEFAULT NULL,
  created_by VARCHAR(255) NOT NULL,
  esxi VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
