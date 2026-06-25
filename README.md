<p style="font-family:verdana, font-size:60px">autoMETAte</p>

# what is it?

autoMETAte is a pre-commit hook made to fill out a metadata file for your software. It was created with the intended use for the academic world, but it is open source with an MIT license meaning anyone is welcome to use it as they wish.

Metadata is important to have in order for people to effectively find your work when refining their search. As part of the scientific process it is important to make sure a record of the work done is available and can direct members of the public and fellow researchers towards it. But, nobody wants another admin task to do, so I created this tool to do it for you.


# how does it work?

It is a pre-commit hook, meaning that it will run when you commit your work to git (whether you store your code in github, codeberg, gitlab, or another service). To use it you need to install [precommit](https://pre-commit.com/#install) and add this repository to the `.pre-commit-config.yaml` file and it will run and update your metadata file everytime you make a commit. That way your metadata is always up to date and you can continue doing what you do best!
