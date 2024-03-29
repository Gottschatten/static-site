#! /usr/bin/env zsh
#
#start tmux session for programming
#
#set -e 

SESSIONNAME=$(pwd)
tmux has-session -t $SESSIONNAME &> /dev/null

if [ $? != 0 ]
  then
    tmux new-session -s $SESSIONNAME -n zsh -d
    tmux new-window -n src -c src
fi

tmux attach -t $SESSIONNAME
    
