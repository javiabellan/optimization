range Scenes = 1..n;
range Days = 1..m;
range Actor = …;
int fee[Actor] = …;

set{Actor} appears[Scenes] = …;
set{int} which[a in Actor] = setof(i in Scenes) member(a,appears[i]);
var{int} shoot[Scenes] in Days;

minimize
  sum(a in Actor) sum(d in Days)
  fee[a] * or(s in which[a]) (shoot[s]=d)
subject to {
  atmost(all(i in Days) 5,Days,shoot);
  scene[1] = 1;
  forall(s in Scenes: s > 1)
  scene[s] <= max(k in 1..s-1) scene[k] + 1; # Break simetry AS A CONSTRAINT !!!!
}