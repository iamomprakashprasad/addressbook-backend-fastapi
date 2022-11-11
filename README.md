This projet is made under hiring process of EastVantage.com by Om Prakash.
The task is to develop an address book by using FastApi


# Steps to setup Project
git clone https://github.com/iamomprakashprasad/fastapi.git
cd fastapi
virtualenv -p python3 venv (for linux)
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app


# Steps to create address in database
Open Postman
Use Post method with url ==> "http://127.0.0.1:8000"
Payload format = {
    "address_coordinate": address_cordinate,
    "address":address
    }

# Steps to get all address
Just a open browser and visit http://127.0.0.1:8000 (or the link flashed in your terminal)
initially no address in database

# Steps to get address by id 
Open a openbrowser and visit http://127.0.0.1:8000/getaddressbyid/{address_id}  address id you get as id while fetching addresses or creating address


# Steps to delete address by id
Open Postman
Use delete method with url ==> "http://127.0.0.1:8000/deleteaddressbyid/{address_id}"

# Steps to update address by id
Open Postman 
Use Put method with url url --> "http://127.0.0.1:8000/updateaddressbyid/{address_id}"
Payload format = {
    "address_coordinate": address_cordinate,
    "address":address
    }

# Steps to get address by Coordinates
Just a open browser and visit http://127.0.0.1:8000/getaddressbycooordinate/{address_coordinate} (or the link flashed in your terminal)
it will show multiple addresses if multiple addresses were created at same cordinate.