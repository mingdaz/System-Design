---
layout: post
title:  "Design Search Typeahead"
date:   2018-05-03 08:00:00
categories: 
tags: [ ]
---

<div class="row">
      <div id="problem-box" class="col-xs-12 ">
        <div ng-app="course" ng-controller="CourseController as courses" ng-init="init(&quot;{\&quot;title\&quot;:\&quot;Search Typeahead service\&quot;,\&quot;statement\&quot;:\&quot;\\u003ch5\\u003eDesign a search typeahead ( Search autocomplete ) system at Google’s scale.\\u003c/h5\\u003e \\u003cimg src='https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/search_typeahead_intro.png'\\u003e\&quot;,\&quot;sections\&quot;:[{\&quot;cases\&quot;:[{\&quot;type\&quot;:\&quot;mandatory\&quot;,\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eHow many typeahead suggestions are to be provided? \\u003cbr /\\u003e\\u003cb\\u003eA: \\u003c/b\\u003e Let's assume 5 for this case. \&quot;},{\&quot;type\&quot;:\&quot;extra\&quot;,\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eDo we need to account for spelling mistakes ? \\u003cbr /\\u003e\\u003cb\\u003eA: \\u003c/b\\u003e Example : Should typing \\u003ci\\u003emik\\u003c/i\\u003e give michael as a suggestion because michael is really popular as a query? \\u003cbr /\\u003e Lets assume we need not account for spelling mistakes, and assume that the suggestions will have the typed phrase as the strict prefix.\&quot;},{\&quot;type\&quot;:\&quot;extra\&quot;,\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eWhat is the criteria for choosing the 5 suggestions ? \\u003cbr /\\u003e\\u003cb\\u003eA: \\u003c/b\\u003e As the question suggests, all suggestions should have the typed phrase/query as the strict prefix. Now amongst those, the most relevant would be the most popular 5. Here, popularity of a query can be determined by the frequency of the query being searched in the past.\&quot;},{\&quot;type\&quot;:\&quot;extra\&quot;,\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eDoes the system need to be realtime ( For example, recent popular events like “Germany wins the FIFA worldcup” starts showing up in results within minutes ).\\u003cbr /\\u003e\\u003cb\\u003eA: \\u003c/b\\u003e Let's assume that it needs to be realtime.\&quot;},{\&quot;type\&quot;:\&quot;extra\&quot;,\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eDo we need to support personalization with the suggestions? ( My interests / queries affect the search suggestions shown to me). \\u003cbr /\\u003e\\u003cb\\u003eA: \\u003c/b\\u003e Let's assume that we don’t need to support personalization\&quot;}],\&quot;next_step\&quot;:\&quot;Estimate number of searches per second\&quot;},{\&quot;name\&quot;:\&quot;Estimations\&quot;,\&quot;questions\&quot;:[{\&quot;text\&quot;:\&quot;\\u003cp\\u003e There are essentialy 2 parts to this system : \\u003cul style='list-style-type:disc'\\u003e  \\u003cli\\u003eClients can query my system for top 5 suggestions given a query prefix.\\u003c/li\\u003e \\u003cli\\u003eEvery search query done should feed into the system for an update. \\u003c/li\\u003e \\u003c/ul\\u003eLets estimate the volume of each. \\u003c/p\\u003e \\u003cb\\u003eQ: \\u003c/b\\u003e How many search queries are done per day?\&quot;,\&quot;intro\&quot;:\&quot; How many queries should we handle?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e Assuming the scale of Google, we can expect around 2-4 Billion queries per day.\&quot;,\&quot;next_step\&quot;:\&quot;How many queries per second should the system handle?\&quot;,\&quot;id\&quot;:353001,\&quot;discourse_id\&quot;:3221},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e How many queries per second should the system handle?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e We can use the estimation from the last question here. \\u003cbr /\\u003e Total Number of queries : 4 Billion \\u003cbr /\\u003e Average length of query : 5 words = 25 letters ( Since avg length of english word is 5 letters ).  \\u003cbr /\\u003e Assuming, every single keystroke results in a typeahead query, we are looking at an upper bound of 4 x 25 = 100 Billion queries per day.\&quot;,\&quot;next_step\&quot;:\&quot;How much data would we need to store?\&quot;,\&quot;id\&quot;:353002,\&quot;discourse_id\&quot;:3222},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e How much data would we need to store?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e Lets first look at the amount of new data we generate every day. 15% of the search queries are new for Google ( ~500 Million new queries ). Assuming 25 letters on average per query, we will 12.5G new data per day. \\u003cbr /\\u003e Assuming, we have accumulated queries over the last 10 years, the size would be 12.5 * 365 * 10 G which is approximately 50TB.\&quot;,\&quot;next_step\&quot;:\&quot;Let's list down our Design Goals\&quot;,\&quot;id\&quot;:353003,\&quot;discourse_id\&quot;:3223}]},{\&quot;name\&quot;:\&quot;Design Goals\&quot;,\&quot;questions\&quot;:[{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e Is Latency a very important metric for us?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e A big Yes. Search typeahead almost competes with typing speed and hence needs to have a really low latency.\&quot;,\&quot;next_step\&quot;:\&quot;Consistency?\&quot;,\&quot;intro\&quot;:\&quot;How important is Latency for us?\&quot;,\&quot;id\&quot;:353004,\&quot;discourse_id\&quot;:3228},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e How important is Consistency for us?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e  Not really important. If 2 people see different top 5 suggestions which are on the same scale of popularity, its not the end of the world. I, as a product owner, am happy as long as the results become eventually consistent.\&quot;,\&quot;next_step\&quot;:\&quot;Availability?\&quot;,\&quot;id\&quot;:353005,\&quot;discourse_id\&quot;:3229},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e How important is Availability for us?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e Very important. If search typeahead is not available, the site would still keep working. However, it will lead to a much degraded experience.\&quot;,\&quot;next_step\&quot;:\&quot;Skeleton of the design\&quot;,\&quot;id\&quot;:353006,\&quot;discourse_id\&quot;:3230}]},{\&quot;name\&quot;:\&quot;Skeleton of the design\&quot;,\&quot;questions\&quot;:[{\&quot;text\&quot;:\&quot;\\u003cp\\u003eAs discussed before, there are essentially 2 parts to this system : \\u003cbr /\\u003e \\u003cul style='list-style-type:circle'\\u003e \\u003cli\\u003eGiven a query, give me 5 most frequent search terms with the query as strict prefix \\u003c/li\\u003e \\u003cli\\u003e Given a search term, update the frequencies. \\u003c/li\\u003e \\u003c/ul\\u003e \\u003c/p\\u003e \\u003cbr /\\u003e \\u003cb\\u003eQ: \\u003c/b\\u003e What would the API look like for the client?\&quot;,\&quot;intro\&quot;:\&quot;What would the API look like for the client?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e \\u003cdiv class='code-block'\\u003e \\u003cdiv\\u003e Read: List(string) getTopSuggestions(string currentQuery) \\u003cbr /\\u003e Write: void updateSuggestions(string searchTerm)\\u003c/div\\u003e \\u003c/div\\u003e \&quot;,\&quot;next_step\&quot;:\&quot;How should we store the the data?\&quot;,\&quot;id\&quot;:353007,\&quot;discourse_id\&quot;:3231},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eWhat is a good data structure to store my search queries so that I can quickly retrieve the top 5 most popular queries?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e For this question, we need to figure out top queries with another string as strict prefix. If you have dealt with enough string questions, you would realize a prefix tree (or trie) would be a perfect fit here. \\u003cbr /\\u003e Devil however lies in the details. We will dig deeper into the nitty gritty of this in the next section.\&quot;,\&quot;next_step\&quot;:\&quot;How would a typical read query look like?\&quot;,\&quot;id\&quot;:353008,\&quot;discourse_id\&quot;:3232},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e How would a typical read query look like?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eComponents: \\u003cbr /\\u003e \\u003cul style='list-style-type:disc'\\u003e \\u003cli\\u003e Client ( Mobile app / Browser, etc ) which calls getTopSuggestions(currentQuery) \\u003c/li\\u003e \\u003cli\\u003eApplication server which interprets the API call and queries the database for the corresponding top 5 queries.\\u003c/li\\u003e \\u003cli\\u003eDatabase server which looks up the top queries in the trie.\\u003c/li\\u003e \\u003c/ul\\u003e \\u003cimg src='https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_read.jpg'\\u003e\&quot;,\&quot;next_step\&quot;:\&quot;How would a typical write query look like?\&quot;,\&quot;id\&quot;:353009,\&quot;discourse_id\&quot;:3233},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eHow would a typical write query look like?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eComponents: \\u003cbr /\\u003e \\u003cul style='list-style-type:disc'\\u003e \\u003cli\\u003e Client ( Mobile app / Browser, etc ) which calls updateSuggestions(searchTerm) \\u003c/li\\u003e \\u003cli\\u003eApplication server which interprets the API call and forwards the searchTerm to database for update.\\u003c/li\\u003e \\u003cli\\u003eDatabase server which updates its trie using the searchTerm\\u003c/li\\u003e \\u003c/ul\\u003e \\u003cimg src='https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_write.jpg'\\u003e\&quot;,\&quot;next_step\&quot;:\&quot;Let's deep dive into the design?\&quot;,\&quot;id\&quot;:353010,\&quot;discourse_id\&quot;:3234}]},{\&quot;name\&quot;:\&quot;Deep Dive\&quot;,\&quot;questions\&quot;:[{\&quot;text\&quot;:\&quot;\\u003cp\\u003e Lets dig deeper into every component one by one. \\u003cbr /\\u003e \\u003ch5\\u003eApplication layer:\\u003c/h5\\u003e  \\u003ci\\u003eThink about all details/gotchas yourself before beginning.\\u003c/i\\u003e \\u003cbr /\\u003e   \\u003c/p\\u003e  \\u003cb\\u003eQ: \\u003c/b\\u003e How would you take care of application layer fault tolerance?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e If we have only one application server machine, our whole service would become unavailable. Machines will fail and so will network. So, we need to plan for those events. Multiple application server machines along with load balancer is the way to go.\&quot;,\&quot;explanation\&quot;:{\&quot;questions\&quot;:[{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eHow do we handle the case where our application server dies?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eThe simplest thing that could be done here is to have multiple application server. They do not store any data (stateless) and all of them behave the exact same way when up. So, if one of them goes down, we still have other application servers who would keep the site running.\&quot;,\&quot;next_step\&quot;:\&quot;How would we know when a machine dies?\&quot;,\&quot;id\&quot;:353021,\&quot;discourse_id\&quot;:3236},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eHow does our client know which application servers to talk to. How does it know which application servers have gone down and which ones are still working?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eWe introduce load balancers. Load balancers are a set of machines (an order of magnitude lower in number) which track the set of application servers which are active ( not gone down ). Client can send request to any of the load balancers who then forward the request to one of the working application servers randomly.\&quot;,\&quot;next_step\&quot;:\&quot;Database layer?\&quot;,\&quot;id\&quot;:353022,\&quot;discourse_id\&quot;:3237}],\&quot;text\&quot;:\&quot;\&quot;},\&quot;intro\&quot;:\&quot;Application layer fault tolerance?\&quot;,\&quot;next_step\&quot;:\&quot;Database layer?\&quot;,\&quot;id\&quot;:353011,\&quot;discourse_id\&quot;:3235},{\&quot;text\&quot;:\&quot;\\u003cp\\u003e\\u003ch5\\u003eDatabase layer:\\u003c/h5\\u003e Let's first dig deeper into the trie we talked about earlier.\\u003c/p\\u003e \\u003cbr /\\u003e \\u003cb\\u003eQ: \\u003c/b\\u003e How would a read query on the trie work?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eThe read query would require us to fetch the top 5 results per query. A traditional trie would store the frequency of the search term ending on the node n1 at n1. In such a trie, how do we get the 5 most frequent queries which have the search term as strict prefix. Obviously, all such frequent queries would be the terms in the subtree under n1 ( as shown in diagram ). \\u003cbr /\\u003e So, a bruteforce way is to scan all the nodes in the subtree and find the 5 most frequent. Lets estimate the number of nodes we will have to scan this way. \\u003cbr /\\u003e Lets say, the user just typed one letter ‘a’. In such a case, we would end up scanning all queries which begin with ‘a’. As we discussed earlier, this would mean scanning terabytes of data which is clearly very time taking and inefficient. Also, the high latency does not align with our design goals. \\u003cimg src='https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_1.jpg'\\u003e \\u003cimg src='https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_2.jpg'\\u003e\&quot;,\&quot;next_step\&quot;:\&quot;How can we make read more efficient?\&quot;,\&quot;id\&quot;:353012,\&quot;discourse_id\&quot;:3238},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eHow can we modify the trie so that reads become super efficient?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eStorage is cheap. Lets say we were allowed to store more stuff on each node. How would we use the extra storage to reduce the latency of answering the query. \\u003cbr /\\u003e A good choice would be storing the top 5 queries for the prefix ending on node n1 at n1 itself. So, every node has the top 5 search terms from the subtree below it. The read operation becomes fairly simple now. Given a search prefix, we traverse down to the corresponding node and return the top 5 queries stored in that node. \\u003cimg src='https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_3.jpg'\\u003e\&quot;,\&quot;explanation\&quot;:{\&quot;text\&quot;:\&quot;\\u003cb\\u003eHint\\u003c/b\\u003e : Store more data on every node of the trie. \&quot;},\&quot;next_step\&quot;:\&quot;How would a typical write work in this trie?\&quot;,\&quot;id\&quot;:353013,\&quot;discourse_id\&quot;:3239},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eHow would a typical write work in this trie?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e So, now whenever we get an actual search term, we will traverse down to the node corresponding to it and increase its frequency. But wait, we are not done yet. We store the top 5 queries in each node. Its possible that this particular search query jumped into the top 5 queries of a few other nodes. We need to update the top 5 queries of those nodes then. How do we do it then? Truthfully, we need to know the frequencies of the top 5 queries ( of every node in the path from root to the node ) to decide if this query becomes a part of the top 5. \\u003cbr /\\u003e There are 2 ways we could achieve this. \\u003cdiv style='margin-left: 30px'\\u003e \\u003cul style='list-style-type:circle'\\u003e \\u003cli\\u003eAlong with the top 5 on every node, we also store their frequency. Anytime, a node’s frequency gets updated, we traverse back from the node to its parent till we reach the root. For every parent, we check if the current query is part of the top 5. If so, we replace the corresponding frequency with the updated frequency. If not, we check if the current query’s frequency is high enough to be a part of the top 5. If so, we update the top 5 with frequency.\\u003c/li\\u003e  \\u003cli\\u003eOn every node, we store the top pointer to the end node of the 5 most frequent queries ( pointers instead of the text ). The update process would involve comparing the current query’s frequency with the 5th lowest node’s frequency and update the node pointer with the current query pointer if the new frequency is greater.\\u003c/li\\u003e \\u003c/ul\\u003e\&quot;,\&quot;next_step\&quot;:\&quot;Can frequent writes affect read efficiency ?\&quot;,\&quot;id\&quot;:353014,\&quot;discourse_id\&quot;:3240},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eCan frequent writes affect read efficiency?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e Yes, potentially. If we are updating the top 5 queries or the frequencies very frequently, we will need to take a lock on the node to make sure the reader thread does not get an inconsistent value. As such, writes start to compete with reads.\&quot;,\&quot;next_step\&quot;:\&quot;Optimizations for read query?\&quot;,\&quot;id\&quot;:353015,\&quot;discourse_id\&quot;:3241},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eWhat optimizations can we do to improve read efficiency?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eAs mentioned earlier, writes compete with read. Sampling writes and Offline updates can be used to improve read efficieny. \\u003cbr /\\u003e\&quot;,\&quot;explanation\&quot;:{\&quot;questions\&quot;:[{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eCan we use sampling?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eYes. If we assume Google’s scale, most frequent queries would appear 100s of times in an hour. As such instead of using every query to update, we can sample 1 in 100 or 1 in 1000 query and update the trie using that.\&quot;,\&quot;next_step\&quot;:\&quot;Another hint\&quot;,\&quot;id\&quot;:353023,\&quot;discourse_id\&quot;:3243},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eOffline update?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eAgain if we assume that most queries appearing in the search typeahead would appear 100s of times in an hour, we can have an offline hashmap which keeps maintaining a map from query to frequency. Its only when the frequency becomes a multiple of a threshold that we go and update the query in the trie with the new frequency. The hashmap being a separate datastore would not collide with the actual trie for reads.\&quot;,\&quot;next_step\&quot;:\&quot;Can we use an updated copy of trie to improve read efficiency?\&quot;,\&quot;id\&quot;:353024,\&quot;discourse_id\&quot;:3244}]},\&quot;next_step\&quot;:\&quot;Can we use an updated copy of trie to improve read efficiency?\&quot;,\&quot;id\&quot;:353016,\&quot;discourse_id\&quot;:3242},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eWhat if I use a separate trie for updates and copy it over to the active one periodically?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eNot really, there are 2 major problems with this approach.\\u003cbr /\\u003e \\u003cul style='list-style-type:circle'\\u003e \\u003cli\\u003e You are not realtime anymore. Lets say you copy over the trie every hour. Its possible a search term became very popular and it wasn’t reflected for an hour because it was present in the offline trie and did not appear till it was copied to the original trie \\u003c/li\\u003e \\u003cli\\u003e The trie is humungous. Copying over the trie can’t be an atomic operation. As such, how would you make sure that reads are still consistent while still processing incoming writes?  \\u003c/li\\u003e \\u003c/ul\\u003e\&quot;,\&quot;next_step\&quot;:\&quot;Would all data fit on a single machine?\&quot;,\&quot;id\&quot;:353017,\&quot;discourse_id\&quot;:3245},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eWould all data fit on a single machine?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eRefer to estimations section. We would need to store more than 50TB of data. \\u003cbr /\\u003eIdeally, we would want most of it in memory to help with the latency. Thats a lot to ask from a single machine. We will go with a “No” here.\&quot;,\&quot;next_step\&quot;:\&quot;How do we shard the data then?\&quot;,\&quot;id\&quot;:353018,\&quot;discourse_id\&quot;:3246},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eAlright, how do we shard the data then?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eLets say we were sharding till the second or third level and we optimize for load here. Lets also say that we have the data around the expected load for every prefix. \\u003cbr /\\u003e We keep traversing the 2 letter prefixes in order ('a', 'aa', 'ab', 'ac',...) and break when the total load exceeds an threshold load and assign that range to a shard. \\u003cbr /\\u003e We will need to have a master which has this mapping with it, so that it can route a prefix query to the correct shard.\&quot;,\&quot;explanation\&quot;:{\&quot;questions\&quot;:[{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e Would we only shard on the first level?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eThe number of shards could very well be more than the number of branches on first level(26). We will need to be more intelligent than just sharding on first level.\&quot;,\&quot;next_step\&quot;:\&quot;What if we assign have a separate shard for each branch?\&quot;,\&quot;id\&quot;:353025,\&quot;discourse_id\&quot;:3248},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003e What is the downside of assigning one branch to a different shard?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003e Load imbalance. Storage imbalance. Some letters are more frequent than the others. For example, letters starting with 'a' are more likely than letters starting with 'x'. As such, we can run into cases of certain shards running hot on load. Also, certain shards will have to store more data because there are more queries starting with a certain letter. Another fact in favor of sharding a little more intelligently.\&quot;,\&quot;next_step\&quot;:\&quot;How would we handle a DB machine going down?\&quot;,\&quot;id\&quot;:353026,\&quot;discourse_id\&quot;:3249}]},\&quot;next_step\&quot;:\&quot;How would we handle a DB machine going down?\&quot;,\&quot;id\&quot;:353019,\&quot;discourse_id\&quot;:3247},{\&quot;text\&quot;:\&quot;\\u003cb\\u003eQ: \\u003c/b\\u003eHow would we handle a DB machine going down?\&quot;,\&quot;answer\&quot;:\&quot;\\u003cb\\u003eA: \\u003c/b\\u003eAs we discussed earlier, availability is more important to us than consistency. If thats the case, we can maintain multiple replica of each shard and an update goes to all replicas. The read can go to multiple replicas (not necessarily all) and uses the first response it gets. If a replica goes down, reads and writes continue to work fine as there are other replicas to serve the queries. \\u003cbr /\\u003e The issue occurs when this replica comes back up. There are 2 options here : \\u003cul style='list-style-type:circle'\\u003e \\u003cli\\u003e If the frequency of the replica going down is lower or we have much higher number of replicas, the replica which comes back up can read the whole data from one of the older working replica while keeping the new incoming writes in a queue. \\u003c/li\\u003e \\u003cli\\u003e There is a queue with every server which contains the changelog or the exact write query being sent to them. The replica can request any of the other replicas in its shard for all changelog since a particular timestamp and use that to update its trie. \\u003c/li\\u003e \\u003c/ul\\u003e\&quot;,\&quot;next_step\&quot;:\&quot;\&quot;,\&quot;id\&quot;:353020,\&quot;discourse_id\&quot;:3250}]}]}&quot;, true)" class="ng-scope">
          <div class="panel panel-default gray problem-statement">
            <div class="panel-heading">
              <h1 class="panel-title pull-left">Design Search Typeahead</h1>
                  <button id="add-bookmark" data-add-bookmark-url="/courses/2/topics/19/problems/design-search-typeahead/add-bookmark/" data-remove-bookmark-url="/courses/2/topics/19/problems/design-search-typeahead/remove-bookmark/" data-bookmarked="false" class="pull-right bookmark-btn bm-green" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Add to bookmarks (can be accessed from dashboard)">
                    Bookmark </button>
              <div class="clearfix"></div>
            </div>
            <div class="panel-body">
              <div id="problem-content" class="markdown-content subjective-problem" style="position: relative; min-height: 420px;">
                    <div id="problem-complete-graph-ct" class="hidden-xs" style="display: none;">
  <div id="problem-complete-graph"></div>
  <div id="problem-complete-percent">40%</div>
</div>
<div class="" ng-hide="!showTimeLine || false" id="vertical-line"></div>
<div class="main" style="" id="system-design-root">
  <div id="comment-url" data-comment-url="https://www.interviewbit.com/courses/system-design/topics/interview-questions/problems/design-search-typeahead/"></div>
  <h2 class="text-center problem-desc ng-binding" ng-bind-html="renderHtml(problem['statement'])" style="font-size: 16px"><h5>Design a search typeahead ( Search autocomplete ) system at Google’s scale.</h5> <img src="https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/search_typeahead_intro.png"></h2>

  <!-- ngIf: show_features --><div ng-if="show_features" class="ng-scope">
    <hr>
    <h4> <br> Features: </h4>
    <blockquote class="newEl"> <p> This is the first part of any system design interview, coming up with the features which the system should support. As an interviewee, you should try to list down all the features you can think of which our system should support. Try to spend around 2 minutes for this section in the interview. You can use the notes section alongside to remember what you wrote. </p> </blockquote>
  </div><!-- end ngIf: show_features -->

  <ul style="list-style-type:circle">
    <!-- ngRepeat: feature in features_shown --><li class="question-background-main list-group newEl" ng-repeat="feature in features_shown">
      <span class="question-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[0])"><b>Q: </b>How many typeahead suggestions are to be provided? </span>
      <br>
      <span class="answer-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[1])"><b>A: </b> Let's assume 5 for this case. </span>
    </li><!-- end ngRepeat: feature in features_shown --><li class="question-background-main list-group newEl" ng-repeat="feature in features_shown">
      <span class="question-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[0])"><b>Q: </b>Do we need to account for spelling mistakes ? </span>
      <br>
      <span class="answer-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[1])"><b>A: </b> Example : Should typing <i>mik</i> give michael as a suggestion because michael is really popular as a query? </span>
    </li><!-- end ngRepeat: feature in features_shown --><li class="question-background-main list-group newEl" ng-repeat="feature in features_shown">
      <span class="question-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[0])"><b>Q: </b>What is the criteria for choosing the 5 suggestions ? </span>
      <br>
      <span class="answer-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[1])"><b>A: </b> As the question suggests, all suggestions should have the typed phrase/query as the strict prefix. Now amongst those, the most relevant would be the most popular 5. Here, popularity of a query can be determined by the frequency of the query being searched in the past.</span>
    </li><!-- end ngRepeat: feature in features_shown --><li class="question-background-main list-group newEl" ng-repeat="feature in features_shown">
      <span class="question-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[0])"><b>Q: </b>Does the system need to be realtime ( For example, recent popular events like “Germany wins the FIFA worldcup” starts showing up in results within minutes ).</span>
      <br>
      <span class="answer-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[1])"><b>A: </b> Let's assume that it needs to be realtime.</span>
    </li><!-- end ngRepeat: feature in features_shown --><li class="question-background-main list-group newEl" ng-repeat="feature in features_shown">
      <span class="question-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[0])"><b>Q: </b>Do we need to support personalization with the suggestions? ( My interests / queries affect the search suggestions shown to me). </span>
      <br>
      <span class="answer-text ng-binding" ng-bind-html="renderHtml(feature.text.split('<br />')[1])"><b>A: </b> Let's assume that we don’t need to support personalization</span>
    </li><!-- end ngRepeat: feature in features_shown -->
  </ul>


  <!-- ngIf: sections_visible[1] --><div ng-if="sections_visible[1]" class="ng-scope">
    <hr>
    <br><br>
    <h4> Estimation: </h4>
    <blockquote> <p class="newEl"> This is usually the second part of a design interview, coming up with the estimated numbers of how scalable our system should be. Important parameters to remember for this section is the number of queries per second and the data which the system will be required to handle. <br> Try to spend around 5 minutes for this section in the interview. </p> </blockquote>
  </div><!-- end ngIf: sections_visible[1] -->

  <!-- ngRepeat: question in sections_shown[1]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[1]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><p> There are essentialy 2 parts to this system : </p><ul style="list-style-type:disc">  <li>Clients can query my system for top 5 suggestions given a query prefix.</li> <li>Every search query done should feed into the system for an update. </li> </ul>Lets estimate the volume of each. <p></p> <b>Q: </b> How many search queries are done per day?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> Assuming the scale of Google, we can expect around 2-4 Billion queries per day.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px; ">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">1</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[1]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[1]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b> How many queries per second should the system handle?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> We can use the estimation from the last question here. <br> Total Number of queries : 4 Billion <br> Average length of query : 5 words = 25 letters ( Since avg length of english word is 5 letters ).  <br> Assuming, every single keystroke results in a typeahead query, we are looking at an upper bound of 4 x 25 = 100 Billion queries per day.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px; ">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">3</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[1]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[1]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b> How much data would we need to store?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> Lets first look at the amount of new data we generate every day. 15% of the search queries are new for Google ( ~500 Million new queries ). Assuming 25 letters on average per query, we will 12.5G new data per day. <br> Assuming, we have accumulated queries over the last 10 years, the size would be 12.5 * 365 * 10 G which is approximately 50TB.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px; ">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">6</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[1]['questions'] -->


  <!-- ngIf: sections_visible[2] --><div ng-if="sections_visible[2]" class="ng-scope">
    <hr>
    <br><br>
    <h4> Design Goals: </h4>
    <blockquote class="newEl">
      <ul>
        <li><b>Latency</b> - Is this problem very latency sensitive (Or in other words, Are requests with high latency and a failing request, equally bad?). For example, search typeahead suggestions are useless if they take more than a second.</li>
        <li><b>Consistency</b> - Does this problem require tight consistency? Or is it okay if things are eventually consistent?</li>
        <li><b>Availability</b> - Does this problem require 100% availability?</li>
      </ul>
      <i>There could be more goals depending on the problem.
        It's possible that all parameters might be important, and some of them might conflict. In that case, you’d need to prioritize one over the other.</i>
    </blockquote>
  </div><!-- end ngIf: sections_visible[2] -->


  <!-- ngRepeat: question in sections_shown[2]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[2]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b> Is Latency a very important metric for us?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> A big Yes. Search typeahead almost competes with typing speed and hence needs to have a really low latency.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[2]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[2]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b> How important is Consistency for us?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>  Not really important. If 2 people see different top 5 suggestions which are on the same scale of popularity, its not the end of the world. I, as a product owner, am happy as long as the results become eventually consistent.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[2]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[2]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b> How important is Availability for us?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> Very important. If search typeahead is not available, the site would still keep working. However, it will lead to a much degraded experience.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[2]['questions'] -->


  <!-- ngIf: sections_visible[3] --><div ng-if="sections_visible[3]" class="ng-scope">
    <hr>
    <br><br>
    <h4> Skeleton of the design: </h4>
    <blockquote> <p class="newEl">
      The next step in most cases is to come up with the barebone design of your system, both in terms of API and the overall workflow of a read and write request.
      Workflow of read/write request here refers to specifying the important components and how they interact.
      Try to spend around 5 minutes for this section in the interview. <br>
      <b>Important</b> : Try to gather feedback from the interviewer here to indicate if you are headed in the right direction.
    </p>
    </blockquote>
  </div><!-- end ngIf: sections_visible[3] -->


  <!-- ngRepeat: question in sections_shown[3]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[3]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><p>As discussed before, there are essentially 2 parts to this system : <br> </p><ul style="list-style-type:circle"> <li>Given a query, give me 5 most frequent search terms with the query as strict prefix </li> <li> Given a search term, update the frequencies. </li> </ul> <p></p> <br> <b>Q: </b> What would the API look like for the client?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> <div class="code-block"> <div> Read: List(string) getTopSuggestions(string currentQuery) <br> Write: void updateSuggestions(string searchTerm)</div> </div> </div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">3</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[3]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[3]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>What is a good data structure to store my search queries so that I can quickly retrieve the top 5 most popular queries?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> For this question, we need to figure out top queries with another string as strict prefix. If you have dealt with enough string questions, you would realize a prefix tree (or trie) would be a perfect fit here. <br> Devil however lies in the details. We will dig deeper into the nitty gritty of this in the next section.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">2</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[3]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[3]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b> How would a typical read query look like?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>Components: <br> <ul style="list-style-type:disc"> <li> Client ( Mobile app / Browser, etc ) which calls getTopSuggestions(currentQuery) </li> <li>Application server which interprets the API call and queries the database for the corresponding top 5 queries.</li> <li>Database server which looks up the top queries in the trie.</li> </ul> <img src="https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_read.jpg"></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[3]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[3]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>How would a typical write query look like?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>Components: <br> <ul style="list-style-type:disc"> <li> Client ( Mobile app / Browser, etc ) which calls updateSuggestions(searchTerm) </li> <li>Application server which interprets the API call and forwards the searchTerm to database for update.</li> <li>Database server which updates its trie using the searchTerm</li> </ul> <img src="https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_write.jpg"></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[3]['questions'] -->


  <!-- ngIf: sections_visible[4] --><div ng-if="sections_visible[4]" class="ng-scope">
    <hr>
    <br><br>
    <h4> Deep Dive: </h4>
    <blockquote> <p class="newEl"> Lets dig deeper into every component one by one. Discussion for this section will take majority of the interview time(20-30 minutes).</p> </blockquote>
  </div><!-- end ngIf: sections_visible[4] -->


  <!-- ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><p> Lets dig deeper into every component one by one. <br> </p><h5>Application layer:</h5>  <i>Think about all details/gotchas yourself before beginning.</i> <br>   <p></p>  <b>Q: </b> How would you take care of application layer fault tolerance?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] --><div class="newEl question-background ng-scope" style="margin-left: 30px" ng-repeat="q in question['explanation']['questions']">
        <div class="container-fluid" style="padding-left: 0; padding-right: 0;">
          <div ng-bind-html="renderHtml(q['text'])" style="padding: 0px" class="col-md-11 question-text ng-binding"><b>Q: </b>How do we handle the case where our application server dies?</div>
          <div class="col-md-1">
            <!-- ngIf: q['count'] != undefined --><div ng-if="q['count'] != undefined" class="pull-right ng-scope">
              <a ng-click="getComments(q, $event)" href="">
                <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
                  <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
                  <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
                </span></a>
            </div><!-- end ngIf: q['count'] != undefined -->
          </div>
        </div>
        <!-- ngIf: q['explanation'] -->
        <!-- ngIf: q['answer'] --><div ng-if="q['answer']" ng-bind-html="renderHtml(q['answer'])" class="ng-binding ng-scope"><b>A: </b>The simplest thing that could be done here is to have multiple application server. They do not store any data (stateless) and all of them behave the exact same way when up. So, if one of them goes down, we still have other application servers who would keep the site running.</div><!-- end ngIf: q['answer'] -->
        <br>
      </div><!-- end ngRepeat: q in question['explanation']['questions'] --><div class="newEl question-background ng-scope" style="margin-left: 30px" ng-repeat="q in question['explanation']['questions']">
        <div class="container-fluid" style="padding-left: 0; padding-right: 0;">
          <div ng-bind-html="renderHtml(q['text'])" style="padding: 0px" class="col-md-11 question-text ng-binding"><b>Q: </b>How does our client know which application servers to talk to. How does it know which application servers have gone down and which ones are still working?</div>
          <div class="col-md-1">
            <!-- ngIf: q['count'] != undefined --><div ng-if="q['count'] != undefined" class="pull-right ng-scope">
              <a ng-click="getComments(q, $event)" href="">
                <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
                  <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
                  <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
                </span></a>
            </div><!-- end ngIf: q['count'] != undefined -->
          </div>
        </div>
        <!-- ngIf: q['explanation'] -->
        <!-- ngIf: q['answer'] --><div ng-if="q['answer']" ng-bind-html="renderHtml(q['answer'])" class="ng-binding ng-scope"><b>A: </b>We introduce load balancers. Load balancers are a set of machines (an order of magnitude lower in number) which track the set of application servers which are active ( not gone down ). Client can send request to any of the load balancers who then forward the request to one of the working application servers randomly.</div><!-- end ngIf: q['answer'] -->
        <br>
      </div><!-- end ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> If we have only one application server machine, our whole service would become unavailable. Machines will fail and so will network. So, we need to plan for those events. Multiple application server machines along with load balancer is the way to go.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><p></p><h5>Database layer:</h5> Let's first dig deeper into the trie we talked about earlier.<p></p> <br> <b>Q: </b> How would a read query on the trie work?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>The read query would require us to fetch the top 5 results per query. A traditional trie would store the frequency of the search term ending on the node n1 at n1. In such a trie, how do we get the 5 most frequent queries which have the search term as strict prefix. Obviously, all such frequent queries would be the terms in the subtree under n1 ( as shown in diagram ). <br> So, a bruteforce way is to scan all the nodes in the subtree and find the 5 most frequent. Lets estimate the number of nodes we will have to scan this way. <br> Lets say, the user just typed one letter ‘a’. In such a case, we would end up scanning all queries which begin with ‘a’. As we discussed earlier, this would mean scanning terabytes of data which is clearly very time taking and inefficient. Also, the high latency does not align with our design goals. <img src="https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_1.jpg"> <img src="https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_2.jpg"></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">2</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>How can we modify the trie so that reads become super efficient?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] --><div ng-if="question['explanation']['text']" ng-bind-html="renderHtml(question['explanation']['text'])" class="newEl ng-binding ng-scope"><b>Hint</b> : Store more data on every node of the trie. </div><!-- end ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>Storage is cheap. Lets say we were allowed to store more stuff on each node. How would we use the extra storage to reduce the latency of answering the query. <br> A good choice would be storing the top 5 queries for the prefix ending on node n1 at n1 itself. So, every node has the top 5 search terms from the subtree below it. The read operation becomes fairly simple now. Given a search prefix, we traverse down to the corresponding node and return the top 5 queries stored in that node. <img src="https://dajh2p2mfq4ra.cloudfront.net/assets/site-images/system_design/typeahead_3.jpg"></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">3</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>How would a typical write work in this trie?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> So, now whenever we get an actual search term, we will traverse down to the node corresponding to it and increase its frequency. But wait, we are not done yet. We store the top 5 queries in each node. Its possible that this particular search query jumped into the top 5 queries of a few other nodes. We need to update the top 5 queries of those nodes then. How do we do it then? Truthfully, we need to know the frequencies of the top 5 queries ( of every node in the path from root to the node ) to decide if this query becomes a part of the top 5. <br> There are 2 ways we could achieve this. <div style="margin-left: 30px"> <ul style="list-style-type:circle"> <li>Along with the top 5 on every node, we also store their frequency. Anytime, a node’s frequency gets updated, we traverse back from the node to its parent till we reach the root. For every parent, we check if the current query is part of the top 5. If so, we replace the corresponding frequency with the updated frequency. If not, we check if the current query’s frequency is high enough to be a part of the top 5. If so, we update the top 5 with frequency.</li>  <li>On every node, we store the top pointer to the end node of the 5 most frequent queries ( pointers instead of the text ). The update process would involve comparing the current query’s frequency with the 5th lowest node’s frequency and update the node pointer with the current query pointer if the new frequency is greater.</li> </ul></div></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">5</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>Can frequent writes affect read efficiency?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b> Yes, potentially. If we are updating the top 5 queries or the frequencies very frequently, we will need to take a lock on the node to make sure the reader thread does not get an inconsistent value. As such, writes start to compete with reads.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">4</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>What optimizations can we do to improve read efficiency?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] --><div class="newEl question-background ng-scope" style="margin-left: 30px" ng-repeat="q in question['explanation']['questions']">
        <div class="container-fluid" style="padding-left: 0; padding-right: 0;">
          <div ng-bind-html="renderHtml(q['text'])" style="padding: 0px" class="col-md-11 question-text ng-binding"><b>Q: </b>Can we use sampling?</div>
          <div class="col-md-1">
            <!-- ngIf: q['count'] != undefined --><div ng-if="q['count'] != undefined" class="pull-right ng-scope">
              <a ng-click="getComments(q, $event)" href="">
                <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
                  <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
                  <i class="fa fa-stack-1x"><span class="ng-binding">2</span></i>
                </span></a>
            </div><!-- end ngIf: q['count'] != undefined -->
          </div>
        </div>
        <!-- ngIf: q['explanation'] -->
        <!-- ngIf: q['answer'] --><div ng-if="q['answer']" ng-bind-html="renderHtml(q['answer'])" class="ng-binding ng-scope"><b>A: </b>Yes. If we assume Google’s scale, most frequent queries would appear 100s of times in an hour. As such instead of using every query to update, we can sample 1 in 100 or 1 in 1000 query and update the trie using that.</div><!-- end ngIf: q['answer'] -->
        <br>
      </div><!-- end ngRepeat: q in question['explanation']['questions'] --><div class="newEl question-background ng-scope" style="margin-left: 30px" ng-repeat="q in question['explanation']['questions']">
        <div class="container-fluid" style="padding-left: 0; padding-right: 0;">
          <div ng-bind-html="renderHtml(q['text'])" style="padding: 0px" class="col-md-11 question-text ng-binding"><b>Q: </b>Offline update?</div>
          <div class="col-md-1">
            <!-- ngIf: q['count'] != undefined --><div ng-if="q['count'] != undefined" class="pull-right ng-scope">
              <a ng-click="getComments(q, $event)" href="">
                <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
                  <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
                  <i class="fa fa-stack-1x"><span class="ng-binding">3</span></i>
                </span></a>
            </div><!-- end ngIf: q['count'] != undefined -->
          </div>
        </div>
        <!-- ngIf: q['explanation'] -->
        <!-- ngIf: q['answer'] --><div ng-if="q['answer']" ng-bind-html="renderHtml(q['answer'])" class="ng-binding ng-scope"><b>A: </b>Again if we assume that most queries appearing in the search typeahead would appear 100s of times in an hour, we can have an offline hashmap which keeps maintaining a map from query to frequency. Its only when the frequency becomes a multiple of a threshold that we go and update the query in the trie with the new frequency. The hashmap being a separate datastore would not collide with the actual trie for reads.</div><!-- end ngIf: q['answer'] -->
        <br>
      </div><!-- end ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>As mentioned earlier, writes compete with read. Sampling writes and Offline updates can be used to improve read efficieny. <br></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">1</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>What if I use a separate trie for updates and copy it over to the active one periodically?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>Not really, there are 2 major problems with this approach.<br> <ul style="list-style-type:circle"> <li> You are not realtime anymore. Lets say you copy over the trie every hour. Its possible a search term became very popular and it wasn’t reflected for an hour because it was present in the offline trie and did not appear till it was copied to the original trie </li> <li> The trie is humungous. Copying over the trie can’t be an atomic operation. As such, how would you make sure that reads are still consistent while still processing incoming writes?  </li> </ul></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">3</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>Would all data fit on a single machine?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>Refer to estimations section. We would need to store more than 50TB of data. <br>Ideally, we would want most of it in memory to help with the latency. Thats a lot to ask from a single machine. We will go with a “No” here.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>Alright, how do we shard the data then?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] --><div class="newEl question-background ng-scope" style="margin-left: 30px" ng-repeat="q in question['explanation']['questions']">
        <div class="container-fluid" style="padding-left: 0; padding-right: 0;">
          <div ng-bind-html="renderHtml(q['text'])" style="padding: 0px" class="col-md-11 question-text ng-binding"><b>Q: </b> Would we only shard on the first level?</div>
          <div class="col-md-1">
            <!-- ngIf: q['count'] != undefined --><div ng-if="q['count'] != undefined" class="pull-right ng-scope">
              <a ng-click="getComments(q, $event)" href="">
                <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
                  <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
                  <i class="fa fa-stack-1x"><span class="ng-binding">1</span></i>
                </span></a>
            </div><!-- end ngIf: q['count'] != undefined -->
          </div>
        </div>
        <!-- ngIf: q['explanation'] -->
        <!-- ngIf: q['answer'] --><div ng-if="q['answer']" ng-bind-html="renderHtml(q['answer'])" class="ng-binding ng-scope"><b>A: </b>The number of shards could very well be more than the number of branches on first level(26). We will need to be more intelligent than just sharding on first level.</div><!-- end ngIf: q['answer'] -->
        <br>
      </div><!-- end ngRepeat: q in question['explanation']['questions'] --><div class="newEl question-background ng-scope" style="margin-left: 30px" ng-repeat="q in question['explanation']['questions']">
        <div class="container-fluid" style="padding-left: 0; padding-right: 0;">
          <div ng-bind-html="renderHtml(q['text'])" style="padding: 0px" class="col-md-11 question-text ng-binding"><b>Q: </b> What is the downside of assigning one branch to a different shard?</div>
          <div class="col-md-1">
            <!-- ngIf: q['count'] != undefined --><div ng-if="q['count'] != undefined" class="pull-right ng-scope">
              <a ng-click="getComments(q, $event)" href="">
                <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
                  <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
                  <i class="fa fa-stack-1x"><span class="ng-binding">0</span></i>
                </span></a>
            </div><!-- end ngIf: q['count'] != undefined -->
          </div>
        </div>
        <!-- ngIf: q['explanation'] -->
        <!-- ngIf: q['answer'] --><div ng-if="q['answer']" ng-bind-html="renderHtml(q['answer'])" class="ng-binding ng-scope"><b>A: </b> Load imbalance. Storage imbalance. Some letters are more frequent than the others. For example, letters starting with 'a' are more likely than letters starting with 'x'. As such, we can run into cases of certain shards running hot on load. Also, certain shards will have to store more data because there are more queries starting with a certain letter. Another fact in favor of sharding a little more intelligently.</div><!-- end ngIf: q['answer'] -->
        <br>
      </div><!-- end ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>Lets say we were sharding till the second or third level and we optimize for load here. Lets also say that we have the data around the expected load for every prefix. <br> We keep traversing the 2 letter prefixes in order ('a', 'aa', 'ab', 'ac',...) and break when the total load exceeds an threshold load and assign that range to a shard. <br> We will need to have a master which has this mapping with it, so that it can route a prefix query to the correct shard.</div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">2</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] --><div class="question-start ng-scope" ng-repeat="question in sections_shown[4]['questions']">
    <p>
    </p><div ng-bind-html="renderHtml(question['text'])" class="newEl question-text question-background-main ng-binding"><b>Q: </b>How would we handle a DB machine going down?</div>
    <!-- ngIf: question['explanation'] --><div ng-if="question['explanation']" class="ng-scope">
      <!-- ngRepeat: q in question['explanation']['questions'] -->
      <!-- ngIf: question['explanation']['text'] -->
    </div><!-- end ngIf: question['explanation'] -->
    <!-- ngIf: question['answer'] --><div ng-if="question['answer']" class="container-fluid question-background-main answer-text ng-scope">
      <div ng-bind-html="renderHtml(question['answer'])" class="newEl col-md-11 ng-binding"><b>A: </b>As we discussed earlier, availability is more important to us than consistency. If thats the case, we can maintain multiple replica of each shard and an update goes to all replicas. The read can go to multiple replicas (not necessarily all) and uses the first response it gets. If a replica goes down, reads and writes continue to work fine as there are other replicas to serve the queries. <br> The issue occurs when this replica comes back up. There are 2 options here : <ul style="list-style-type:circle"> <li> If the frequency of the replica going down is lower or we have much higher number of replicas, the replica which comes back up can read the whole data from one of the older working replica while keeping the new incoming writes in a queue. </li> <li> There is a queue with every server which contains the changelog or the exact write query being sent to them. The replica can request any of the other replicas in its shard for all changelog since a particular timestamp and use that to update its trie. </li> </ul></div>
      <div class="pull-right">
        <!-- ngIf: question['count'] != undefined --><div ng-if="question['count'] != undefined" class="col-md-1 ng-scope">
          <a ng-click="getComments(question, $event)" href="">
            <span class="fa-stack fa-2x comment-icon" style="font-size: 16px;">
              <i class="fa fa-comment fa-stack-2x" style="font-size: 2em;"></i>
              <i class="fa fa-stack-1x"><span class="ng-binding">1</span></i>
            </span></a>
        </div><!-- end ngIf: question['count'] != undefined -->
      </div>
    </div><!-- end ngIf: question['answer'] -->
    <p></p>
  </div><!-- end ngRepeat: question in sections_shown[4]['questions'] -->


  <!-- ngIf: sections_visible[5] -->


  <!-- ngRepeat: question in sections_shown[5]['questions'] -->


  <div align="center" style="margin-top: 12px;">
    <!-- ngIf: encouragement_text -->
    <!-- ngIf: show_explain_button -->
    <!-- ngIf: show_next_button -->
    <br>
    <br>
        
  </div>

  <div id="problem_finished" style="" align="center" class="newEl">
        <i class="fa fa-trophy" style="font-size: larger;"></i> You have now mastered this problem!
  </div>

</div>


              </div>
            </div>
          </div>
        </div>
      </div>
          <div id="problem-note" class="col-xs-12 col-sm-3 hidden">
            <div class="panel panel-default hint-panel" id="notes-panel" style="width: 254px; box-shadow: none; background-color: rgb(248, 248, 248);">
  <div class="panel-heading">
    <h3 class="panel-title pull-left">Notes</h3>
        <a href="/profile/mingda-zhang/notes/?ref=problem-page" class="pull-right">All Notes</a>
    <span class="clearfix"></span>
  </div>

  <form id="notes-form" action="/courses/2/topics/19/problems/353/save-notes/">
    <input type="hidden" name="notes_content" id="hidden_notes">
    <div style="position: relative;">
      <pre class=" ace_editor ace-solarized-light" style="font-size: 12px; height: 463px;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 15px; width: 7.20031px; left: 4px; top: 0px;"></textarea><div class="ace_gutter" style="display: none;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px;"></div><div class="ace_gutter-active-line" style="top: 0px; height: 15px;"></div></div><div class="ace_scroller" style="left: 0px; right: 0px; bottom: 0px;"><div class="ace_content" style="margin-top: 0px; width: 253px; height: 493px; margin-left: 0px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 580.025px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height:15px;top:0px;left:0;right:0;"></div></div><div class="ace_layer ace_text-layer" style="padding: 0px 4px;"><div class="ace_line_group" style="height:15px"><div class="ace_line" style="height:15px"></div></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="left: 4px; top: 0px; width: 7.20031px; height: 15px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 20px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 20px; height: 15px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 20px; left: 0px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 20px; width: 253px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></pre>
      <input type="hidden" class="btn btn-info" value="Save" id="notes-save-btn" data-url="/courses/2/topics/19/problems/design-search-typeahead/save-notes/">
    </div>
  </form>

    <br>
        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">Similar Problems</h3>
          </div>
          <ul class="list-group">
                    <li class="list-group-item">
                      <a href="/problems/design-url-shortener/?ref=similar_problems" class="ga-event-track" data-warn-msg="Average time taken to solve this problem is <span class='time-to-solve'>45</span> minutes. The quicker you solve the problem, the higher the score. Ready to start?<br /><br />" data-defer-access="true" data-eventaction="similiar_problems">
                        Design URL Shortener
                      </a>
                    </li>
          </ul>
        </div>

    <div class="panel panel-success successful-submissions">
      <div class="panel-body">
        <span class="submission-count">5397</span> successful submissions.
      </div>
    </div>

</div>
          </div>
    </div>
