# GitAvatarPrint
Print your github user ( or organisations users) profile avatars into a print ready pdf 

=== 
Dependencies 

    Pillow
    PyPDF2
    requests

Installations

    # Install virtual wrapper
    pip install virtualenvwrapper
    mkvirtualenv gitprint 
    
    # activate virtual env
    workon gitprint
    
    git clone https://github.com/sidja/GitAvatarPrint
    cd GitAvatarprint 
    pip install -r requirements.txt

python git_print.py -u <github_username>

===
##Output Screenshot
![image]

[image]: https://dl.dropboxusercontent.com/u/4318926/Github/git_avatar_print/generated_ex.PNG
