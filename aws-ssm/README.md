# aws-ssm
Amazon EC2 Simple Systems Manager (SSM) is an Amazon Web Services tool that allows us to automatically configure virtual servers in a cloud

1) install_apache_document.yaml is used to run command line script to install Apache
in AWS systems-manager-> documents -> create document and - choose Command documents and run command yaml

2) aws ssm get-parameters --names /my-app/dev/db-url /my-app/dev/db-password --with-decryption
