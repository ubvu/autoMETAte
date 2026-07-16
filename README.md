<p style="font-family:verdana, font-size:60px">autoMETAte</p>

# what is it?

autoMETAte is a pre-commit hook made to fill out a metadata file for your software. It was created with the intended use for the academic world, but it is open source with an MIT license meaning anyone is welcome to use it as they wish.

Metadata is important to have in order for people to effectively find your work when refining their search. As part of the scientific process it is important to make sure a record of the work done is available and can direct members of the public and fellow researchers towards it. But, nobody wants another admin task to do, so I created this tool to do it for you.


# how does it work?

It is a pre-commit hook, meaning that it will run when you commit your work to git (whether you store your code in github, codeberg, gitlab, or another service). To use it you need to install [precommit](https://pre-commit.com/#install) and add this repository to the `.pre-commit-config.yaml` file and it will run and update your metadata file everytime you make a commit. That way your metadata is always up to date and you can continue doing what you do best!

Your `.pre-commit-config.yaml` file can be written with any text editor or IDE and should contain the following lines:

```
- repo: https://github.com/ubvu/autoMETAte
  rev: v0.4.4-alpha
  hooks:
    - id: autometate
```

# what is to come?

This project is currently in alpha and so there is more to come. In its current form it has some of the basics completed, but ideally every field in the metadata will have atleast one mechanism to try to automate it and automation of the DOI is likely to be next. For more information on the progression of the project check out the [issues page](https://github.com/ubvu/autoMETAte/issues). Equally, if you find a bug or have a request then add it as an issue.

Beyond the plans for the code itself there are also plans to connect with services like [Yoda](https://github.com/UtrechtUniversity/Yoda) and [Zenodo](https://zenodo.org/) to meet their metadata requirements and allow the metadata files to be uploaded or automatically read. This should improve the spreading of metadata adoption and save the effort of having to fill out the forms yourself.
