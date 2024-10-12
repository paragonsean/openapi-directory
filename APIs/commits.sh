#!/bin/bash

# Function to push changes to the current branch
push_branch() {
    branch=$1
    echo "Switching to branch $branch"
    
    # Checkout the branch
    git checkout "$branch"

    # Check if there are any changes to commit and push
    if [ "$(git status --porcelain)" ]; then
        echo "Committing and pushing changes on branch $branch"
        
        # Add, commit, and push changes
        git add .
        git commit -m "Automated commit: pushing changes to $branch"
        git push origin "$branch"
    else
        echo "No changes to push on branch $branch"
    fi
}

# Get the list of branches
branches=$(git branch | sed 's/^[* ] //')

# Loop through each branch and push it
for branch in $branches; do
    push_branch "$branch"
    
    # Wait for one minute before pushing the next branch
    echo "Waiting for 1 minute before switching to the next branch..."
    sleep 60
done

echo "All branches have been processed."
