README.md
> “_In computer science, garbage collection is a form of automatic memory management. The garbage collector attempts to reclaim memory which was allocated by the program, but is no longer referenced–also called garbage._”

__Code isn’t meant to be memorized__ – it’s meant to be referenced. Referencing code saves time in our coding projects, as well space in our own minds!__

__Garbage Collection__ is a code snippet management application. It stores code snippets and commits them to memory, _so you don’t have to_. Users can contribute code snippets, for public or private use, and save them to their profile for easy referencing. Code snippet customization is possible with ‘edit’ and ‘delete’ features. Create a free account and start collecting garbage.

\----------------------------------------------------------------------------------------------

__How snippets work:__

Snippets are made up of specific bits of code (required), the code’s unique language (required), a title and description (required), and optional category tags. Each snippet should clearly explain the functionality of the code.

Once a user creates a profile, they can start ‘collecting garbage’ by copying a code snippet to their own profile. The user can utilize the code snippet for their own project, and also edit and republish the changed code on Garbage Collection.

__How copying works:__

The user copies a snippet by clicking a button that creates a link to the original snippet. This feature can be accomplished by utilizing a foreign key. Copying the code instead of favoriting it preserves the original code while also allowing for it to change over time.

__How search works:__

When searching through the garbage collection, the search should sort through titles, descriptions, language, and other tags associated with each snippet.

\---------------------------------------------------------------------------------------
 
__To use on your own computer:__

Clone this repository onto your local computer. Using your command line, run `pipenv install` to make sure your project is up to date with the various tools we use, such as Pillow and Highlight.js. After installation, `run makemigrations`. Now you’re all set to run the server, which uses the URL <http://127.0.0.1:8000/>, with the command, `python manage.py runserver`. Create an account to gain access to the application.


___Happy Code Rummaging!__
