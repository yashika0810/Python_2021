
### SOPS_GPG Automation Script: 

This section holds the instructions to run the `sops_gpg.sh` script in order to set the secrets (add/replace) and encypt & decrypt the secrets. You can find this script in `bin/sops_gpg.sh`

#### 1. Please make sure to configure AWS CLI
#### 2. Configure the variable "GPG_URL" in which you need to provide the URL of the s3 bucket where GPG key is stored. You need to only provide it once. It will download the GPG_KEY.asc on your local. 
#### 3. Configure the variable "SECRET_FILE" to the required secret file. The default is set to `secrets.staging.enc.yaml`

#### 4. There are three input parameters required to run the script -


* Command

* Secret Key

* Secret Value

#### Example to run script :

```
./sops_gpg.sh set-secret --key <key>  --value <value> 

```
The above command will the following oepration:
* Decrypt the secrets
* Adds/Replace key value to the secrets. If the key already exists, it will update the value to the same key
* Encrypt the updated file


> NOTE: The decrypted secrets will be deleted once the encryption is performed.
