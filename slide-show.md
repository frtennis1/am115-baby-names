Presentation Slide Show
=======================

Modeling United States Baby Name Popularity Across Time and Space
-----------------------------------------------------------------

- The US Census publishes number of births by baby name each state and year
  (e.g. ”Emily” was the most popular baby girl name in 2000: 25,953 born that
  year)

- We wish to understand the dynamics by which names propagate and “diffuse” in
  popularity across time (names have popularity persistence) and across space
  (names sometimes jump from a neighboring state to another)

- Potentially, we would like to be able to use our model to also predict future
  popular baby names

Mathematical Model
------------------

- We intend to approach this problem by building on top of the diffusion
  framework we have discussed in class, and applying it to name popularity with
  some modifications

- Stylistically, names cluster in popularity geographically, and follow a
  life-cycle of booming into popularity and then fading as another name booms
  after it. We wish to capture this kind of behavior through a diffusion model



