

# fmucc

## What does it do
A small template repository that converts a source code FMU to a target platform (win64/linux64) binary FMU through `git push`. 

## How to do it
- Create a new github repo by clicking the `Use this template` button in this repo.
- Make sure you have an [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) account.
    - You can have 10 free open source projects with unlimited minutes [ref](https://azure.microsoft.com/en-us/services/devops/pipelines/)
- Create an Azure pipeline project linked to your newly created repo.
- `git pull` the repo to local.
- Add your to-be-compiled source code FMUs to `./fmus` folder.
    - Additionally, you can set a specific target platform by setting `compileLinux64` or `compileWin64` within `azure-pipelines.yml`.
- Commit changes and `git push`.
- An Azure pipline running [fmpy](https://github.com/CATIA-Systems/FMPy) should be triggered automatically to compile the added FMUs.
- Once done, download binary FMUs from artifact.

## Acknowledgements
- [fmpy](https://github.com/CATIA-Systems/FMPy)
- [Azure pipeline](https://azure.microsoft.com/en-us/services/devops/pipelines/)



