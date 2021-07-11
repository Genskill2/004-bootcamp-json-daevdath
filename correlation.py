# Add the functions in this file
import json
import math 

def load_journal(fname:str)->dict:
 json_data=open(fname,"r")
 data=json.loads(json_data)
 return data
 
def compute_phi(fname:str,event:str)->float:
 data=load_journal(fname)
 corr=0.0
 np1,n1p,np0,n0p=0,0,0,0
 n11,n10,n01,n00=0,0,0,0
 for i in range(len(data)):
  state=dict(data[i])["squirrel"]
  event=dict(data[i])["events"]
  if state==True:
   np1+=1
  else:
   np0+=1
  if event in events:
   n1p+=1
    if(state):
     n11+=1
    else:
     n10+=1
  else:
   n0p+=1
   if(state):
    no1+=1
   else:
    n00+=1  
  corr=((n11*n00)-(n01*n10))/math.sqrt(np1*np0*n1p*n0p)
  return corr
  
def compute_correlations(fname:str)->dict: 
  data=load_journal(fname)
  eventphi={}
  for i in range(len(data)):
   events=data[i]["events"]
   for event in events
    if event not in eventphi 
     eventphi[event]=compute_phi(fname,event)
  return eventphi   
  
def diagnose(fname)->list:
 eventphi=compute_correlations(fname)
 req_list=[]
 max_event=-2
 min_event=2
 for event in eventphi
  if eventphi[event]>max_corr:
   max_event=event
  if eventphi[event]<min_corr:
   min_corr=event
 req_list.append(max_event)
 req_list.append(min_event)
 return req_list   
  
  
