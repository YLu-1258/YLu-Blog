---
keywords: fastai
description: Demonstration of Pandas
title: Intro to Pandas
toc: true
author: Alex Lu
badges: true
comments: true
categories: [jupyter,interests]
nb_path: _notebooks/2023-03-12-Pandas-hack.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2023-03-12-Pandas-hack.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Pandas"><strong>Pandas</strong><a class="anchor-link" href="#Pandas"> </a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I will use a dataset of <a href="https://www.kaggle.com/winston56/fortune-500-data-2021">Fortune 1000</a> from Kaggle datasets to explore pandas library here.</p>
<p>The Fortune 1000 dataset is from the Fortune website. It contains U.S. company data for the year 2021. The dataset is 1000 rows and 18 columns.</p>
<p>Features:</p>
<ul>
<li>Company - values are the name of the company
Rank - The 2021 rank established by Fortune (1-1000)</li>
<li>Rank Change - The change in the rank from 2020 to 2021. There is only a rank change listed if the company is currently in the top 500 and was previously in the top 500.</li>
<li>Revenue - Revenue of each company in millions. This is the criteria used to rank each company.</li>
<li>Profit - Profit of each company in millions.
Num. of Employees - The number of employees each company employs.</li>
<li>Sector - The sector of the market the company operates in.</li>
<li>City - The city where the company's headquarters is located.</li>
<li>State - The state where the company's headquarters is located</li>
<li>Newcomer - Indicates whether or not the company is new to the top Fortune 500 ("yes" or "no"). No value will be listed for companies outside of the top 500.</li>
<li>CEO Founder - Indicates whether the CEO of the company is also the founder ("yes" or "no").</li>
<li>CEO Woman - Indicates whether the CEO of the company is a woman ("yes" or "no").</li>
<li>Profitable - Indicates whether the company is profitable or not ("yes" or "no").</li>
<li>Prev. Rank - The 2020 rank of the company, as established by Fortune. There will only be previous rank data for the top 500 companies.</li>
<li>CEO - The name of the CEO of the company</li>
<li>Website - The url of the company website</li>
<li>Ticker - The stock ticker symbol of public companies. Some rows will have empty values because the company is a private corporation.</li>
<li>Market Cap - The market cap (or value) of the company in millions. Some rows will have empty values because the company is private. Market valuations were determined on January 20, 2021.</li>
</ul>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">!</span>wget -nc /content/ https://datasets21.s3-us-west-1.amazonaws.com/Fortune_1000.csv
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>/content/: Scheme missing.
File ‘Fortune_1000.csv’ already there; not retrieving.

</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">f1000</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;Fortune_1000.csv&#39;</span><span class="p">,</span><span class="n">index_col</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1000</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
Index: 1000 entries, Walmart to Liberty Oilfield Services
Data columns (total 17 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   rank               1000 non-null   int64  
 1   rank_change        1000 non-null   float64
 2   revenue            1000 non-null   float64
 3   profit             998 non-null    float64
 4   num. of employees  1000 non-null   int64  
 5   sector             1000 non-null   object 
 6   city               1000 non-null   object 
 7   state              1000 non-null   object 
 8   newcomer           500 non-null    object 
 9   ceo_founder        1000 non-null   object 
 10  ceo_woman          1000 non-null   object 
 11  profitable         1000 non-null   object 
 12  prev_rank          1000 non-null   object 
 13  CEO                992 non-null    object 
 14  Website            1000 non-null   object 
 15  Ticker             938 non-null    object 
 16  Market Cap         960 non-null    object 
dtypes: float64(3), int64(2), object(12)
memory usage: 140.6+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1000</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rank</th>
      <th>rank_change</th>
      <th>revenue</th>
      <th>profit</th>
      <th>num. of employees</th>
      <th>sector</th>
      <th>city</th>
      <th>state</th>
      <th>newcomer</th>
      <th>ceo_founder</th>
      <th>ceo_woman</th>
      <th>profitable</th>
      <th>prev_rank</th>
      <th>CEO</th>
      <th>Website</th>
      <th>Ticker</th>
      <th>Market Cap</th>
    </tr>
    <tr>
      <th>company</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Walmart</th>
      <td>1</td>
      <td>0.0</td>
      <td>523964.0</td>
      <td>14881.0</td>
      <td>2200000</td>
      <td>Retailing</td>
      <td>Bentonville</td>
      <td>AR</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>yes</td>
      <td>1.0</td>
      <td>C. Douglas McMillon</td>
      <td>https://www.stock.walmart.com</td>
      <td>WMT</td>
      <td>411690</td>
    </tr>
    <tr>
      <th>Amazon</th>
      <td>2</td>
      <td>3.0</td>
      <td>280522.0</td>
      <td>11588.0</td>
      <td>798000</td>
      <td>Retailing</td>
      <td>Seattle</td>
      <td>WA</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>5.0</td>
      <td>Jeffrey P. Bezos</td>
      <td>https://www.amazon.com</td>
      <td>AMZN</td>
      <td>1637405</td>
    </tr>
    <tr>
      <th>Exxon Mobil</th>
      <td>3</td>
      <td>-1.0</td>
      <td>264938.0</td>
      <td>14340.0</td>
      <td>74900</td>
      <td>Energy</td>
      <td>Irving</td>
      <td>TX</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>yes</td>
      <td>2.0</td>
      <td>Darren W. Woods</td>
      <td>https://www.exxonmobil.com</td>
      <td>XOM</td>
      <td>177923</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Select-data-using-those-labels">Select data using those labels<a class="anchor-link" href="#Select-data-using-those-labels"> </a></h3><p>Because the axes in pandas have labels, I can select data using those labels — unlike in NumPy, where I needed to know the exact index location. To do this, I can use the <code>DataFrame.loc[]</code> attribute. The syntax for <code>DataFrame.loc[]</code> is:</p>
<p><code>df.loc[row_label, column_label]</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Select-Single-Column">Select Single Column<a class="anchor-link" href="#Select-Single-Column"> </a></h4>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">companies</span> <span class="o">=</span> <span class="n">f1000</span><span class="o">.</span><span class="n">loc</span><span class="p">[:,</span><span class="s1">&#39;profit&#39;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">companies</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">f1000</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">companies</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>company
Walmart                      14881.0
Amazon                       11588.0
Exxon Mobil                  14340.0
Apple                        55256.0
CVS Health                    6634.0
                              ...   
Mr. Cooper Group               274.0
Herc Holdings                   47.5
Healthpeak Properties           45.5
SPX FLOW                       -95.1
Liberty Oilfield Services       39.0
Name: profit, Length: 1000, dtype: float64
&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
&lt;class &#39;pandas.core.series.Series&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Series-object">Series object<a class="anchor-link" href="#Series-object"> </a></h4>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">f1000</span><span class="o">.</span><span class="n">loc</span><span class="p">[:,</span><span class="s1">&#39;revenue&#39;</span><span class="p">])</span>

<span class="nb">print</span><span class="p">(</span><span class="n">f1000</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s1">&#39;Apple&#39;</span><span class="p">,</span><span class="s1">&#39;revenue&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>company
Walmart                      523964.0
Amazon                       280522.0
Exxon Mobil                  264938.0
Apple                        260174.0
CVS Health                   256776.0
                               ...   
Mr. Cooper Group               2007.0
Herc Holdings                  1999.0
Healthpeak Properties          1997.4
SPX FLOW                       1996.3
Liberty Oilfield Services      1990.3
Name: revenue, Length: 1000, dtype: float64
260174.0
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Select-multiple-columns">Select multiple columns<a class="anchor-link" href="#Select-multiple-columns"> </a></h4><ul>
<li>List of columns</li>
<li>Slice of columns</li>
</ul>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1000</span><span class="p">[[</span><span class="s1">&#39;rank&#39;</span><span class="p">,</span><span class="s1">&#39;revenue&#39;</span><span class="p">]]</span>

<span class="c1">#f1000.loc[:,&#39;rank&#39;:&#39;sector&#39;]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rank</th>
      <th>revenue</th>
    </tr>
    <tr>
      <th>company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Walmart</th>
      <td>1</td>
      <td>523964.0</td>
    </tr>
    <tr>
      <th>Amazon</th>
      <td>2</td>
      <td>280522.0</td>
    </tr>
    <tr>
      <th>Exxon Mobil</th>
      <td>3</td>
      <td>264938.0</td>
    </tr>
    <tr>
      <th>Apple</th>
      <td>4</td>
      <td>260174.0</td>
    </tr>
    <tr>
      <th>CVS Health</th>
      <td>5</td>
      <td>256776.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Mr. Cooper Group</th>
      <td>996</td>
      <td>2007.0</td>
    </tr>
    <tr>
      <th>Herc Holdings</th>
      <td>997</td>
      <td>1999.0</td>
    </tr>
    <tr>
      <th>Healthpeak Properties</th>
      <td>998</td>
      <td>1997.4</td>
    </tr>
    <tr>
      <th>SPX FLOW</th>
      <td>999</td>
      <td>1996.3</td>
    </tr>
    <tr>
      <th>Liberty Oilfield Services</th>
      <td>1000</td>
      <td>1990.3</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 2 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Select-rows-by-labels">Select rows by labels<a class="anchor-link" href="#Select-rows-by-labels"> </a></h4>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1000</span><span class="o">.</span><span class="n">loc</span><span class="p">[[</span><span class="s1">&#39;Amazon&#39;</span><span class="p">,</span> <span class="s1">&#39;Apple&#39;</span><span class="p">]]</span>
<span class="c1">#f1000.loc[&#39;Amazon&#39;:&#39;Apple&#39;]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rank</th>
      <th>rank_change</th>
      <th>revenue</th>
      <th>profit</th>
      <th>num. of employees</th>
      <th>sector</th>
      <th>city</th>
      <th>state</th>
      <th>newcomer</th>
      <th>ceo_founder</th>
      <th>ceo_woman</th>
      <th>profitable</th>
      <th>prev_rank</th>
      <th>CEO</th>
      <th>Website</th>
      <th>Ticker</th>
      <th>Market Cap</th>
    </tr>
    <tr>
      <th>company</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Amazon</th>
      <td>2</td>
      <td>3.0</td>
      <td>280522.0</td>
      <td>11588.0</td>
      <td>798000</td>
      <td>Retailing</td>
      <td>Seattle</td>
      <td>WA</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>5.0</td>
      <td>Jeffrey P. Bezos</td>
      <td>https://www.amazon.com</td>
      <td>AMZN</td>
      <td>1637405</td>
    </tr>
    <tr>
      <th>Apple</th>
      <td>4</td>
      <td>-1.0</td>
      <td>260174.0</td>
      <td>55256.0</td>
      <td>137000</td>
      <td>Technology</td>
      <td>Cupertino</td>
      <td>CA</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>yes</td>
      <td>3.0</td>
      <td>Timothy D. Cook</td>
      <td>https://www.apple.com</td>
      <td>AAPL</td>
      <td>2221176</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Series.value_counts()-method">Series.value_counts() method<a class="anchor-link" href="#Series.value_counts()-method"> </a></h3><p><code>Series.value_counts()</code> method. This method displays each unique non-null value in a column and their counts in order.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sector_value_counts</span> <span class="o">=</span> <span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;sector&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">(</span><span class="n">ascending</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sector_value_counts</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Food &amp; Drug Stores                10
Telecommunications                11
Apparel                           16
Motor Vehicles &amp; Parts            22
Aerospace &amp; Defense               22
Media                             25
Household Products                26
Hotels, Restaurants &amp; Leisure     27
Chemicals                         27
Engineering &amp; Construction        30
Wholesalers                       35
Food, Beverages &amp; Tobacco         37
Transportation                    38
Materials                         46
Industrials                       50
Business Services                 52
Health Care                       71
Retailing                         75
Technology                       109
Energy                           109
Financials                       162
Name: sector, dtype: int64
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;sector&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s1">&#39;Technology&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>109</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can also try to locate what the largest increase or decrease in compay rank were.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#f1000[&#39;rank_change&#39;].max()</span>
<span class="c1">#f1000[&#39;rank_change&#39;].min()</span>
<span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;rank_change&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>count    1000.000000
mean        0.426000
std        22.424169
min      -186.000000
25%         0.000000
50%         0.000000
75%         0.000000
max       224.000000
Name: rank_change, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;rank_change&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre> 0.0     544
-1.0      22
-2.0      18
 2.0      16
 4.0      15
        ... 
-30.0      1
-43.0      1
 98.0      1
 86.0      1
-87.0      1
Name: rank_change, Length: 118, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><em>Example</em>:</p>
<p>List out the numbers of companies in the Fortune 1000 of the top 3 states</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">top_3_states</span> <span class="o">=</span> <span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;state&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">top_3_states</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>CA    121
TX     95
NY     89
Name: state, dtype: int64
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><em>Example:</em></p>
<p>find the company in California that employs the most people  in the dataset.</p>
<p>I can use the <code>DataFrame.sort_values()</code> method to sort the rows on the employees column</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f1000</span><span class="p">[</span><span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;state&#39;</span><span class="p">]</span><span class="o">==</span><span class="s1">&#39;CA&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="s1">&#39;num. of employees&#39;</span><span class="p">,</span><span class="n">ascending</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rank</th>
      <th>rank_change</th>
      <th>revenue</th>
      <th>profit</th>
      <th>num. of employees</th>
      <th>sector</th>
      <th>city</th>
      <th>state</th>
      <th>newcomer</th>
      <th>ceo_founder</th>
      <th>ceo_woman</th>
      <th>profitable</th>
      <th>prev_rank</th>
      <th>CEO</th>
      <th>Website</th>
      <th>Ticker</th>
      <th>Market Cap</th>
    </tr>
    <tr>
      <th>company</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wells Fargo</th>
      <td>30</td>
      <td>-1.0</td>
      <td>103915.0</td>
      <td>19549.0</td>
      <td>259800</td>
      <td>Financials</td>
      <td>San Francisco</td>
      <td>CA</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>yes</td>
      <td>29.0</td>
      <td>Charles W. Scharf</td>
      <td>https://www.wellsfargo.com</td>
      <td>WFC</td>
      <td>99941</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><em>Exercise:</em></p>
<p>find the unique list of states in the dataset</p>
<p>To identify the unique states, I can use the <code>Series.unique()</code> method. This method returns an array of unique values from any series.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">states</span> <span class="o">=</span> <span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;state&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">states</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;AR&#39; &#39;WA&#39; &#39;TX&#39; &#39;CA&#39; &#39;RI&#39; &#39;NE&#39; &#39;MN&#39; &#39;PA&#39; &#39;MI&#39; &#39;CT&#39; &#39;OH&#39; &#39;NY&#39; &#39;IL&#39; &#39;DC&#39;
 &#39;NC&#39; &#39;GA&#39; &#39;IN&#39; &#39;MA&#39; &#39;NJ&#39; &#39;VA&#39; &#39;MO&#39; &#39;TN&#39; &#39;KY&#39; &#39;ID&#39; &#39;MD&#39; &#39;OR&#39; &#39;FL&#39; &#39;WI&#39;
 &#39;CO&#39; &#39;OK&#39; &#39;LA&#39; &#39;DE&#39; &#39;AZ&#39; &#39;IA&#39; &#39;NV&#39; &#39;KS&#39; &#39;AL&#39; &#39;SC&#39; &#39;ND&#39; &#39;NH&#39; &#39;MS&#39; &#39;PR&#39;
 &#39;UT&#39; &#39;HI&#39; &#39;VT&#39; &#39;ME&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong><em>Demonstration:</em></strong></p>
<p>I'm going to produce the following dictionary of the top employer in each state:</p>
<ol>
<li><p>create an empty dictionary, <code>top_employer_by_state</code> to store the results of the exercise.</p>
</li>
<li><p>Use the <code>Series.unique()</code> method to create an array of unique values from the state column</p>
</li>
<li><p>Use a for loop to iterate over the array unique states. In each iteration:</p>
</li>
</ol>
<ul>
<li>Select only the rows that have a state name equal to the current iteration.</li>
<li>Use <code>DataFrame.sort_values()</code> to sort those rows by the <code>num. of employees</code> column in descending order.</li>
<li>Select the first row from the sorted dataframe and convert the Dataframe into a series using <code>DataFrame.squeeze()</code></li>
<li>Extract the company name from the index label company by <code>Series.name</code>.</li>
<li>Assign the results to the top_employer_by_state dictionary, using the state name as the key, and the company name as the value.</li>
</ul>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">top_exmployer_by_state</span> <span class="o">=</span> <span class="p">{}</span>
<span class="n">states</span> <span class="o">=</span> <span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;state&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>

<span class="k">for</span> <span class="n">state</span> <span class="ow">in</span> <span class="n">states</span><span class="p">:</span>
  <span class="n">selected_companies</span> <span class="o">=</span> <span class="n">f1000</span><span class="p">[</span><span class="n">f1000</span><span class="p">[</span><span class="s1">&#39;state&#39;</span><span class="p">]</span><span class="o">==</span><span class="n">state</span><span class="p">]</span>
  <span class="n">top_exmployer_by_state</span><span class="p">[</span><span class="n">state</span><span class="p">]</span> <span class="o">=</span> <span class="n">selected_companies</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="s1">&#39;num. of employees&#39;</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">squeeze</span><span class="p">()</span><span class="o">.</span><span class="n">name</span>
  
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">top_exmployer_by_state</span><span class="p">:</span>
  <span class="nb">print</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="s1">&#39; : &#39;</span><span class="p">,</span> <span class="n">top_exmployer_by_state</span><span class="p">[</span><span class="n">key</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>AR  :  Walmart
WA  :  Amazon
TX  :  Yum China Holdings
CA  :  Wells Fargo
RI  :  CVS Health
NE  :  Berkshire Hathaway
MN  :  Target
PA  :  Aramark
MI  :  Ford Motor
CT  :  XPO Logistics
OH  :  Kroger
NY  :  IBM
IL  :  Walgreens Boots Alliance
DC  :  Danaher
NC  :  Lowe&amp;#8217;s
GA  :  Home Depot
IN  :  Anthem
MA  :  TJX
NJ  :  Cognizant Technology Solutions
VA  :  Hilton Worldwide Holdings
MO  :  Emerson Electric
TN  :  FedEx
KY  :  Humana
ID  :  Albertsons
MD  :  Marriott International
OR  :  Nike
FL  :  Publix Super Markets
WI  :  Kohl&amp;#8217;s
CO  :  VF
OK  :  Helmerich &amp; Payne
LA  :  Lumen Technologies
DE  :  DuPont
AZ  :  Republic Services
IA  :  Casey&amp;#8217;s General Stores
NV  :  MGM Resorts International
KS  :  Yellow
AL  :  Encompass Health
SC  :  Sonoco Products
ND  :  MDU Resources Group
NH  :  PC Connection
MS  :  Sanderson Farms
PR  :  Popular
UT  :  Nu Skin Enterprises
HI  :  Hawaiian Holdings
VT  :  NLV Financial
ME  :  IDEXX Laboratories
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Reference">Reference<a class="anchor-link" href="#Reference"> </a></h2><p><a href="https://pandas.pydata.org/docs/reference/index.html">pandas API reference</a></p>
<p><a href="https://www.javatpoint.com/pandas-vs-numpy#:~:text=The%20Pandas%20module%20mainly%20works,works%20with%20the%20numerical%20data.&amp;text=NumPy%20library%20provides%20objects%20for,memory%20as%20compared%20to%20Pandas.">pandas vs. NumPy</a></p>

</div>
</div>
</div>
</div>
 
