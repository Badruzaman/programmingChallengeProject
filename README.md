
# Python flask web API
This repository contains the source code that I demonstrate in my prgramming challenge.

**Challenge Description:**

Generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.

Sample extracted output:

hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, nmarcysfa900jkifh  , 3.781, 2.11, ....

The output should be 2MB in size. Once file generation is done the output should be available as a link which can be then downloaded by clicking on it. Also, there should be a button on the page so by clicking on this button the total number of each random objects will be displayed.

**Note:** The backend API must be written using Flask (Python). All the communication between frontend and backend MUST be done via these APIs only

# Requirements
* Python 3.9.3
* flask 2.0.1
* flask_cors 3.0.10
* create virtualenv 


# Description
## Three web api I have built for doing the challenge
* /api/v1/generatefile/ for file generate 
* /api/v1/getfile/  for generated file download
* /api/v1/objectcount/ for four type of objects count

## API Detail
Api /api/v1/generatefile is used for generate a file which size is 2MB and returns an URL (API) /api/v1/getfile to be downloaded the generated file
and /api/v1/objectcount counts all four types of object already generated

## Code Detail
I have written app.py for building all Api, and the file service.py is for all required method like generate file and counting objects and these type of job is done through helper.py file and config.py is for having base url 
