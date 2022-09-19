---
layout: post
---
**Lab \#1: Measurements and Graphical Analysis**

**Alex Lu**

**Purpose:**

Given disks of different radii, determine the relationship between the mass and the radius of the disks through graphical method and calculate the uncertainty associated with the measured value. We will learn about linearization and use it to create a mathematical model.

**Materials and Equipment:**

Balance

Meter stick

Circular disks (identical thickness and uniform density but different radii)

Graphic Calculator or online graphing tool

**Procedure:**

1.  > Substitute equations to get a relationship between mass and radius.

2.  > Use the relationship between mass and radius to determine what variable should be processed to linearize the data

3.  > Measure the radius (in cm) of the cylinder with the ruler with one end of the ruler at the center of the disk and the other on the edge.

4.  > Zero out the balance and then measure the mass (in grams) of the cylinder.

5.  > Stack the metal cylinders and measure the collective height of all cylinders. Divide by the total number of cylinders multiplied by 2 to the power of the number of folds to find the height of each individual cylinder.

6.  > Organize the collected data into a data table

7.  > Plot the original radius and mass

8.  > Plot the processed radius and mass

9.  > Plug height and other constants to create a relationship between mass and radius.

**Equations and calculations:**

**Let:**

  - > \(\rho\) be density

  - > \(m\) be mass

  - > \(v\) be volume

  - > \(a\) be the surface area of the cylinder

  - > \(r\) be the radii of the cylinder

  - > \(h\) be the height of the cylinder

**Thus:**

If \(\rho = \ \frac{m}{v}\) and \(v\  = \ ah\) then

\(m\  = \ \rho v\)

\(m\  = \ \rho\text{ah}\)

If \(a = \pi r^{2}\), then

\(m = \rho\pi r^{2}h\)

Since both \(\rho\) and \(\pi\) are constants and \(h\) is negligible, ∴ \(m\  \propto \ r^{2}\)

Since mass is directly proportional to radius squared, the graph could be linearized if \(r^{2}\) is plotted instead.

**Precision and Uncertainty**

1.  > The balanced used to measure the mass of the metal disks was accurate up to a hundredth of a gram, while the ruler used to measure the radius and height of the disks was accurate up to 1 millimeter (0.1 cm). As such, the radius was measured to the nearest hundredth of a centimeter or a tenth of a millimeter.

**Data Tables**

m = mass

r = radii

H = height

**Mass in Grams, Radius and height in cm, and Radius Squared of Each Metal Disk**

| **Disk** | **m (g)** | **h (cm)** | **r (cm)** |  | **r^2 (cm^2)** |
| -------- | --------- | ---------- | ---------- |  | -------------- |
| 1        | 0.07      | 0.0025     | 2.30       |  | 5.29           |
| 2        | 0.14      | 0.0025     | 3.00       |  | 9.0            |
| 3        | 0.25      | 0.0025     | 4.30       |  | 18.49          |
| 4        | 0.37      | 0.0025     | 4.90       |  | 24.01          |
| 5        | 0.73      | 0.0025     | 7.10       |  | 50.41          |

**Graph of Non-Linearized Data:**

![]({{ site.url }}{{ site.baseurl }}/assets/img/2022-08-28-Alex-Lu---Lab-#1_-Measurements-and-Graphical-Analysis-/media/image2.png)

**Equation:** \(y\  = \ 0.0133921x^{2} + 0.112825x - 0.0238674\)

**R<sup>2</sup> :** \(0.9967\)

This graph has **non-linear data** as it’s represented by a **quadratic** model.

**Graph of Linearized Data:**

![]({{ site.url }}{{ site.baseurl }}/assets/img/2022-08-28-Alex-Lu---Lab-#1_-Measurements-and-Graphical-Analysis-/media/image1.png)

**Line of the best fit equation:** \(y = 0.0145569x - 0.000100527\)

**r =** \(0.9983\)

**r<sup>2</sup> =** \(0.9966\ \)

This graph has **linear** data as it’s represented by a **linear** model.

**Analysis Questions:**

**1) What is the independent variable in your y = mx +b formula?**

Considering the mathematic relationship between disk radius r and disk mass m, the independent variable from my line of best fit represents the radius of the disk squared.

**2) What does the slope represent in your y = mx +b formula? Show dimensionally that indeed that is what your slope represents and that the formula is valid dimensionally.**

Using the \(m = \rho v\) equation and the volume relationship, we can express the disk’s mass in terms of the radius and the height in this relationship: \(m = \rho\pi r^{2}h\). Since density (\(\rho\)) and \(\pi\) are constants, and height (\(h\)) is negligible, we can essentially group these 3 constants into one value serving as the coefficient to the radius squared term. Thus, the slope is the product of the density, height, and \(\pi\). Since height has its units expressed in cm, density has units expressed in g/cm³, and \(\pi\) is a constant wth no units, the slope is a combination of all 3 constants and has units of **g/cm<sup>2</sup>**.

Because our slope has units of g/cm<sup>2</sup>, and x represents the radius squared expressed by cm<sup>2</sup>, and since our desired output (\(y\)) is mass in grams (g), the y-intercept (\(b\)) must have a unit of **grams (g)** in order for both sides of the equation to have the same units (grams).

\(g\  = \ \frac{g}{cm^{2}} \cdot cm^{2} + g\)

\(g = g + g\)

\(g = g\)

**3) Should the "b" in your y = mx + b formula be zero? Explain your answer.**

The y-intercept (\(b\)) in my \(y\  = \ mx\  + \ b\) formula shouldn’t be zero unless the data naturally generates a line of best fit that passes through the origin. Forcing the y-intercept to pass through the origin would either alter the slope (\(m\)) or remove the y-intercept completely. This would result in an inaccurate interpretation of the model as the line is no longer set evenly between the data points. Thus we cannot guarantee the model’s integrity for future data points, rendering our model useless.

**4) Measure/estimate the "thickness" of your cylinders. Use that value to find the experimental density of your cylinders. Find a percent difference between your found density and the actual density. The actual material is aluminum.**

\(y = 0.0145569x - 0.000100527\)

\(slope\  = \ \pi\rho h\)

\(\rho\  = \ density\)

\(\rho\  = \ \frac{\text{slope}}{h\pi} = \frac{0.0145569\ \frac{g}{cm^{2}}}{\pi(0.0025cm)} = 1.85\frac{g}{cm^{3}}\)

The density of the metal disks according to my linear model is \(1.85\frac{g}{cm^{3}}\) , Since the metal used in the disk is Aluminum (density = \(2.70\frac{g}{cm^{3}}\)) we can use the following calculations to determine our percent error

\(\%\ Error\  = \left| \frac{Actual\  - \ Expected}{\text{Expected}} \right|*100\%\ \)

\(\%\ Error\  = \ \left| \frac{1.85\frac{g}{cm^{3}} - 2.70\frac{g}{cm^{3}}}{2.70\frac{g}{cm^{3}}} \right|*100\%\  = 31.5\%\ \)

∴ Percent difference = 31.5%

**5) Errors. Make sure you explain why your number is bigger or smaller than (if positive or negative difference.)**

The number that I obtained is smaller than the actual value (31.5% error) because the instruments that we used to measure the disks’ dimensions had inaccuracies. The ruler that we used to measure the disks’ radius is only precise up to millimeters, and the balanced used to measure mass is only accurate up to the hundredth’s place, while actual instruments used to measure the actual value are much more precise. Additionally, the method I used to measure the height of the disks also had inherent inaccuracies, as folding the aluminum disks over each other may create tiny air pockets that add additional magnitude to my measured height, resulting in an inaccurate height measurement. The uncertainty of the ruler and also the inaccurate way of measuring height may have contributed to a greater height value than the actual value, resulting in a lower density value when I divided. Lastly, the disks weren’t in a perfectly circular shape, thus the direction that I measured the disk in might also have affected the end result, as measuring in different directions would produce different radii.

**Synthesis Questions:**

**1) In this experiment, if we had used disks with a greater thickness, would the slope of your best fit line have been different? Would your experimental value for density be the same? Explain.**

Since slope represents the product of thickness, \(\pi\), and density, having a greater measured thickness would result in a much larger slope value. However, our experimental value of density would still be around the same, as an increase in thickness would also result in a proportionally large increase in mass, which will offset the thickness increase.

**2. How would your graph of m versus r2 be different if you had used disks of the same**

**thickness but made out of steel? Draw a second line on your m versus r2 plot that**

**represents disks made of steel.**

The graph would be of m versus r<sup>2</sup> would be different in that the slope of the graph would be much greater, this is because steel has a much higher density of \(7.85\ \frac{g}{cm^{3}}\) compared to aluminum’s \(2.7\ \frac{g}{cm^{3}}\)

![]({{ site.url }}{{ site.baseurl }}/assets/img/2022-08-28-Alex-Lu---Lab-#1_-Measurements-and-Graphical-Analysis-/media/image3.png)

(Note: The blue line is a rough sketch of what the line of best fit would look like on the same scale as the aluminum graph is steel was used instead. This is not an accurate representation, just an approximation)

**3. Another group of students has acquired data for the exact same experiment; however, their disks are made of an unknown material that they are trying to determine. The group's m versus r2 data produced a line of best fit with slope equal to 122 kg/m2. Each disk they measured had the same 0.5 cm thickness. Calculate the density of the unknown material and use the table below to help determine what material their disks are made of.**

Work:

\(Slope\  = \ 122kg/m^{2}\ ,\ h\  = \ 0.5cm,\ slope\  = \ \rho\pi h\)

\(slope\  = 122\frac{\text{kg}}{m^{2}}*(\frac{1000g}{1kg})*(\frac{1m}{100cm})^{2} = 12.2\frac{g}{cm^{2}}\  = \ \rho\pi h\)

\(\rho = \frac{\text{slope}}{\pi h} = \frac{12.2\frac{g}{cm^{2}}}{\pi*0.5cm} = 7.77\frac{g}{cm^{3}}\)

The closet material to a density of \(7.77\frac{g}{cm^{3}}\) is iron, which has a density of \(7.8\frac{g}{cm^{3}}\). The disks are most likely made out of iron.

**Multiple Choice Questions:**

**1. You perform the same experiment, but this time you plot a linear relationship between mass and the circumference of the disks rather than the radius. What is the slope of the linear plot?**

Work:

\(slope\  = \ \rho\pi h\)

\(m\  = \ \rho v = \rho\pi r^{2}h\)

\(v = \pi r^{2}h\)

Let \(c\) be circumference

\(c\  = \ 2\pi r\)

\(c^{2} = 4\pi^{2}r^{2}\)

\(r^{2} = \frac{c^{2}}{4\pi^{2}}\)

\(m = \rho\pi h(\frac{c^{2}}{4\pi^{2}}) = \frac{\rho hc^{2}}{4\pi} = (\frac{\rho h}{4\pi})c^{2}\)

\(\)

Since \(\rho\) (density), h (height), and \(4\pi\) are all constants, these 3 values could be combined to form the slope for the linear plot, which is \((\frac{\text{ph}}{4\pi})\), Hence, **E** is the correct answer choice.

**2. Skipped**

**3. Consider an experiment in which a student measures the mass and diameter of 10**

**different-sized spheres, all made of the same material of uniform density ρ. For this**

**student to create a linear graph relating the mass of the sphere to its radius r, the**

**student would need to plot mass m versus which quantity:**

\(\text{let\ v\ be\ the\ volume\ of\ a\ sphere}\)

\(v = \frac{4}{3}\pi r^{3}\)

\(m\  = \ pv = (\frac{4p\pi}{3})r^{3}\)

Since \((\frac{4p\pi}{3})\) is a constant, the student must plot a linear graph relating m versus the quality of radius cubed. Hence, option **C** is correct.
