***********
**Purpose**
***********
Purpose of this repository is to track my solutions to leetcode problems and provide a record of my progress.

*************************
**Git Command Reminders**
*************************
git status		- lists the current staging. ie, what files are edited / not edited from the branch.
git add <file>		- adds any files that you've worked on to the staging area
git commit -m "comment" - stages changes in preperation to merge with main branch on github

git branch 		- shows you what branch you're in
git branch <branch Name>- Creates a new branch to work in
git checkout <branch name> - moves you into that branch - changes / new files in this branch are only seen in this branch.
git merge <branch name> - merges the <Branch name> changes branch you are in (probably master). 

git remote 		- lists the remote repositories that exist in your repo
git push -u origin master - pushes the commited changes on master to the origin repo on github
git push -d <remote_name> <branchname>   # Delete remote branch when you're done with it = removes it from github. Same as doing it thru the github page

touch .gitignore 	- add all file name/folders you don't want added to git/github here.  