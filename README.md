
## SOPS_GPG Automation Script: 

This section holds the instructions to run the sops_gpg.sh script in order to encrypt/decrypt our secrets. You can find this script in zapp/bin/sops_gpg.sh 

#### 1. Please make sure to configure AWS CLI
#### 2. Configure the variable value "GPG_URL" in which you need to provide the URL of the s3 bucket where GPG key is stored.
#### 3. There are three input parameters required to run the script -

* $1 --> enc/dec => enc: Encrypt || dec: Decrypt

* $2 --> Source file

* $3 --> Destination file

#### Example to run script :

To Encrypt ```bin/sops_gpg.sh enc bin/<source_filename> bin/<destination_filename>```  </br> 

To Decrypt ```bin/sops_gpg.sh dec bin/<source_filename> bin/<destination_filename>```

#### In case you need to change an environment  variable , you need to run one of these 2 command depending on the environment: 


For staging env: </br>

Encrypting secrets: ```bin/sops_gpg.sh enc  bin/secrets.staging.dec.yaml bin/secrets.staging.enc.yaml``` </br> 

Decrypting secrets file : ```bin/sops_gpg.sh dec bin/secrets.staging.enc.yaml bin/secrets.staging.dec.yaml```


For prod env: 

Encrypting secrets: ```bin/sops_gpg.sh enc  bin/secrets.prod.dec.yaml bin/secrets.prod.enc.yaml``` </br> 

Decrypting secrets file: ```bin/sops_gpg.sh dec bin/secrets.prod.enc.yaml bin/secrets.prod.dec.yaml```

# NOTE: The decrypted secrets will be deleted once the encryption is performed after modifications.
