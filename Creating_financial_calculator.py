
homeHTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p><br />Welcome to the Financial Calculator</p>
<p>&nbsp;</p>
<p><a href="calc_home">Calculator</a></p>
<p>&nbsp;</p>
</center>
""".strip()


calc_splashHTML = """
<center>
<!-- OMIS30 HTML Template-->
</center>
"""

calc_splashHTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>

<head>
<style>
body {
  background-color: #fefbd8;
}

h1 {
  background-color: #80ced6;
}

div {
  background-color: #d5f4e6;
}

span {
  background-color: #00D963;
}
</style>
<font size="8">
<p><span>Calculator Home Page</span></p>
</font size>
<p>&nbsp;</p>
</head>

<body>
<style>
body {
  background-color: #fefbd8;
}

h1 {
  background-color: #80ced6;
}

div {
  background-color: #d5f4e6;
}

span {
  background-color: #FFFFFF;
}
</style>
<font size = "6">
<ul>
<span>
<a href="/calc1">Present Value Calculator</a><br><br>
<a href="/calc2">Future Value Calculator</a><br><br>
<a href="/calc3">Compound Interest Calculator</a><br><br>
</span>
</ul>
</font size>
</center>
</body>

<style>
body{
    background-image: url("https://steamuserimages-a.akamaihd.net/ugc/934939171361132585/B9376B13A1959C41A7B29D383345002100D032F2/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true")
}
</style>
""".strip()

calc1HTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to Present Value Calculator Enter your parameters below, then click submit:</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<form action="/calc1result">
<p>Future Value:<br /> <input name="FV" type="text" /> <br /> Rate of Return:<br /> <input name="ROR" type="text" /> <br /> Number Of Payments:<br /> <input name="NOP" type="text" /><br /> <br /> <br /> <input type="submit" value="Submit" /></p>
<p>&nbsp;</p>
<tr>
<td><a href='/calc_home'> Calculator Home </a></td>
<td><p>&nbsp;</p></td>
</tr>
</form>
</center>
""".strip()

calc1resultHTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>The user entered:</p>
<p>&nbsp;</p>
<table>
<tbody>
<tr>
<td>Future Value</td>
<td>{FV_field}</td>
</tr>
<tr>
<td>Rate of Return</td>
<td>{ROR_field}</td>
</tr>
<tr>
<td>Number of Periods</td>
<td>{NOP_field}</td>
</tr>
<tr>
<td>Present Value</td>
<td>{PV_field}</td>
</tr>
<tr>
<td><a href='/calc_home'> Calculator Home </a></td>
<td><p>&nbsp;</p></td>
</tr>
</tbody>
</table>
</center>
""".strip()

calc2HTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to Compound Interest Calculator Enter your parameters below, then click submit:</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<form action="/calc2result">
<p>Investment Amount <br /> <input name="IA" type="text" /> <br /> Number of Years:<br /> <input name="NOY" type="text" /> <br /> Interest Rate:<br /> <input name="IR" type="text" /><br /> <br /> <br /> <input type="submit" value="Submit" /></p>
<p>&nbsp;</p>
<tr>
<td><a href='/calc_home'> Calculator Home </a></td>
<td><p>&nbsp;</p></td>
</tr>
</form>
</center>
""".strip()

calc2resultHTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>The user entered:</p>
<p>&nbsp;</p>
<table>
<tbody>
<tr>
<td>Investment Amount</td>
<td>{IA_field}</td>
</tr>
<tr>
<td>Number of Years</td>
<td>{NOY_field}</td>
</tr>
<tr>
<td>Interest</td>
<td>{IR_field}</td>
</tr>
<tr>
<td>Future Value</td>
<td>{FV_field}</td>
</tr>
<tr>
<td><a href='/calc_home'> Calculator Home </a></td>
<td><p>&nbsp;</p></td>
</tr>
</tbody>
</table>
</center>
""".strip()

calc3HTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to Compound Interest Calculator Enter your parameters below, then click submit:</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<form action="/calc3result">
<p>Investment Amount <br /> <input name="IAMT" type="text" /> <br /> Number of Years:<br /> <input name="NY" type="text" /> <br /> Interest Rate:<br /> <input name="IRT" type="text" /><br /> <br /> <br /> <input type="submit" value="Submit" /></p>
<p>&nbsp;</p>
<tr>
<td><a href='/calc_home'> Calculator Home </a></td>
<td><p>&nbsp;</p></td>
</tr>
</form>
</center>
""".strip()

calc3resultHTML = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>The user entered:</p>
<p>&nbsp;</p>
<table>
<tbody>
<tr>
<td>Investment Amount</td>
<td>{IAMT_field}</td>
</tr>
<tr>
<td>Number of Years</td>
<td>{NY_field}</td>
</tr>
<tr>
<td>Interest</td>
<td>{IRT_field}</td>
</tr>
<tr>
<td>Compound Interest </td>
<td>{CI_field}</td>
</tr>
<tr>
<td><a href='/calc_home'> Calculator Home </a></td>
<td><p>&nbsp;</p></td>
</tr>
</tbody>
</table>
</center>
""".strip()

calcErrorHTML1 = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to the Error Page.</p>
<p>Please enter only numeric values in the fields. Click "Present Value Calculator" to try again.</p>
<p>&nbsp;</p>
<tr>
<td><a href='/calc1'> Present Value Calculator </a></td>
<td><p>&nbsp;</p></td>
</tr>
</center>
""".strip()

calcErrorHTML2 = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to the Error Page.</p>
<p>Please enter only numeric values in the fields. Click "Future Value Calculator" to try again.</p>
<p>&nbsp;</p>
<tr>
<td><a href='/calc2'> Future Value Calculator </a></td>
<td><p>&nbsp;</p></td>
</tr>
</center>
""".strip()

calcErrorHTML3 = """
<center>
<!-- OMIS30 HTML Template-->
<p>&nbsp;</p>
<p>Welcome to the Error Page.</p>
<p>Please enter only numeric values in the fields. Click "Compound Interest Calculator" to try again.</p>
<p>&nbsp;</p>
<tr>
<td><a href='/calc3'> Compound Interest Calculator </a></td>
<td><p>&nbsp;</p></td>
</tr>
</center>
""".strip()