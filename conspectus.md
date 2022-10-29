# Conspectus. Git.

## Git - Version Control System
		The way to track code changes. Track down bugs. Return to previous versions of code
		
		Directory - Folder
		CLI - command line interface
		Repository - Project or folder where the project is kept
		Github - website to host repositories
		Pull request - request to pull your code into another branch
		
#	Git commands:
	git clone - bring a repository that is hosted somewhere to your local machine
	git add - track your files and changes in Git
	commit - save files in get
	git push - Upload git commits to a remote repo, like Github
	git pull - download changes from remote repo
	status - look at the status of the files (modified, new files, etc.)
	git init - initialise a new git repository
	git remote - connecting to a remote repository (Format: git remote add origin {origin})
	git log - log of all commits
	git reset - unstage the changes
		HEAD~1 - unstage already commited changes
		git reset --hard  - completely removes changes

## Push sequence
	git add (use ./filename),
	git commit 
		-m "message" -m "description"
	---Only-for-modified-files:
		git commit -am "message" - skips git add stage
	----
	git push 

## working with branches
	git branch - show branches
		-d {branch-name} - delete a branch
	git checkout {name}- switch between branches
		-b {name} - create a new branch
	git diff {name_of_branch_diff_against} - shows changes and compares versions of the code
	git push --set-upstream **or replace --set-upstream with -u** origin {name_of_the_branch} - push the new branch to github
	git merge {what to merge from} - merge changes from another branch to current branch
		