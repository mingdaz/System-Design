---
layout: post
title:  "DynamoDB and NoSQL"
date:   2018-05-03 08:00:00
categories: [ Database ]
tags: [ ACID, Consisten Hashing, Vector Clock ]
---

## Useful lectures:  
[Memecached Consistent Hashing](https://www.coursera.org/learn/data-manipulation/lecture/b3edj/memcached-consistent-hashing)  
[Consistent Hashing Cont'd](https://www.coursera.org/learn/data-manipulation/lecture/fBtf7/consistent-hashing-cont-d)  
[DynamoDB Vector Clocks](https://www.coursera.org/learn/data-manipulation/lecture/TBkc1/dynamodb-vector-clocks)  
[Vector Clocks Cont'd](https://www.coursera.org/learn/data-manipulation/lecture/DMI58/vector-clocks-cont-d)  

## Basic Implementation:
[用Python写一个NoSQL](http://liuchengxu.org/blog-cn/posts/nosql-in-python/)
[分布式键值存储 Dynamo 的实现原理](https://draveness.me/dynamo)

## Key Features
#### [Consistent Hashing](https://en.wikipedia.org/wiki/Consistent_hashing)
Load balancing and easy to horizontal scale.

#### [Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))
Read and write need Quorom protocal to return success or value. Parameter `N`, `R` and `W` handle the balance between avaiability and consistency. 

#### [Vector Clock](https://en.wikipedia.org/wiki/Vector_clock)
Gaurantee eventual consistency. Strategies
1. Last write win
2. User decide

#### [Gossip](https://en.wikipedia.org/wiki/Gossip_protocol)
When adding or deleting nodes.