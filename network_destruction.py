#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:33:16 2020
@author: eric
"""
import sys


if sys.argv[1]=="-c":
    f=open(sys.argv[3], "r")
    if f.mode == 'r':
        contents =f.readlines()
    a = contents[0][0] 
    b =contents[0][2]  
    counter2 = sys.argv[2]
    counter = int(counter2)
    maxtable=[]
    graph = {}
    for i in range(len(contents)):
        a = contents[i]
        contents[i]=a.split()
       
        if contents[i][0] not in graph:
            
            graph[contents[i][0]]= [contents[i][1]]
        else:
            graph[contents[i][0]].append(contents[i][1])
        if contents[i][1] not in graph:
            
            graph[contents[i][1]]=[contents[i][0]]
        else:
            graph[contents[i][1]].append(contents[i][0])
            
    graph2 = {}
    for key in graph:
     graph2[key] = graph[key]       
    for value in graph2:
     
       graph2[value]=len(graph[value]) 
    
    for j in range(counter):
     count =0
     count2=0 
     count3=0
     maxtable.clear() 
           
     maxi =0 
     for key in graph:
      graph2[key] = graph[key]       
     for value in graph2:
     
       graph2[value]=len(graph[value]) 
     for i in graph:
         
        pinakas = graph.get(i,"")
        
        if len(pinakas)>= maxi:
            maxi  = len(pinakas)
            p = i
     
     maxistr=str(maxi)
     
     for name, age in graph2.items():  
        if str(age) in maxistr:
         maxtable.append(int(name))
         maxtable.sort()
    
     p = maxtable[0]
     pe = str(p)
     del graph[pe]
     del graph2[pe]
    
     for i in graph.values():
       if pe in i:
            
            i.remove(pe)
     
            
     print(pe,maxi)
elif sys.argv[1]=="-r":
     
     
      f=open(sys.argv[4], "r")
      if f.mode == 'r':
         contents =f.readlines()
      r=sys.argv[2]
      counteri = sys.argv[3]
      counter=int(counteri)
      a = contents[0][0] 
      b =contents[0][2]  
      maxtable=[]
      graph = {}
      for i in range(len(contents)):
        a = contents[i]
        contents[i]=a.split()
       
        if contents[i][0] not in graph:
            
            graph[contents[i][0]]= [contents[i][1]]
        else:
            graph[contents[i][0]].append(contents[i][1])
        if contents[i][1] not in graph:
            
            graph[contents[i][1]]=[contents[i][0]]
        else:
            graph[contents[i][1]].append(contents[i][0])
     
      a=0
      graph3={}
      for key in graph:
        graph3[key]=graph[key]
      graph3={}
      def breadthfirst(graph, start, mdepth):
          
       queue = [start]
       depths = {start: 0}
       while queue:
        queue.reverse()
        vertex = queue.pop()
        queue.reverse()
        if depths[vertex] == mdepth:
            break
        for neighbour in graph[vertex]:
            if neighbour in depths:
                continue
            queue.append(neighbour)
            depths[neighbour] = depths[vertex] + 1
       return depths
      for i in range(counter):
          for i in graph:
              rin = int(r)
              
             
              graph2={}
              for key in graph:
               graph2[key] = graph[key]       
              for value in graph2:
             
               graph2[value]=len(graph[value]) 
              c=0
              depths=breadthfirst(graph,i,rin)
              for l in depths:
                  
                     if depths[l]==rin:
                         c = c + (graph2[l]-1)
                    
                      
              CI =(graph2[i]-1)*c
              graph3[i]=CI
             
          max=0
          for i in graph3:
             if graph3[i]>max:
                 max=graph3[i]
                 
          maxtable2=[]
          for i in graph3:
              if max == graph3[i]:
                  maxtable2.append(int(i))
                  maxtable2.sort()
          dope = str(maxtable2[0])
          print(maxtable2[0],graph3[dope])
          
          del graph[dope]
          del graph2[dope]
          del graph3[dope]
          for i in graph.values():
           if dope in i:
                
                i.remove(dope)
          
     
