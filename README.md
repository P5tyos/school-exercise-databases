<h1>SXED - Employee and Department Management System</h1>

<p>This repository contains a Python school exercise for managing departments and employees using both <strong>MySQL</strong> and <strong>SQLite</strong> backends.</p>

<h2>🧩 What this project does</h2>

<ul>
  <li>Lets users choose between a MySQL or SQLite database backend.</li>
  <li>Supports department and employee CRUD operations:</li>
  <li> - Create, update, delete, and list departments.</li>
  <li> - Create, update, delete, and list employees.</li>
  <li> - Search departments by name.</li>
  <li> - List employees by department.</li>
</ul>

<h2>📁 Files included</h2>

<ul>
  <li><code>main_sxed.py</code> - Main command-line interface and program flow.</li>
  <li><code>class_menuNav.py</code> - Menu display and database selection logic.</li>
  <li><code>class_DBmySQL.py</code> - MySQL backend implementation.</li>
  <li><code>class_DBsqLite.py</code> - SQLite backend implementation.</li>
  <li><code>class_department.py</code> - Department domain object.</li>
  <li><code>class_employee.py</code> - Employee domain object.</li>
</ul>

<h2>⚙️ Requirements</h2>

<ul>
  <li>Python 3.13 or later.</li>
  <li><strong>For MySQL mode:</strong> a running MySQL server and a valid user with access to a database.</li>
  <li><strong>For SQLite mode:</strong> no external server is required.</li>
  <li>Python package <code>pymysql</code> installed for MySQL support.</li>
</ul>

<h2>📝 Important usage notes</h2>

<ul>
  <li>The program is a school exercise and several design decisions were guided by the teacher.</li>
  <li>Some database structure and CLI organization were chosen to practice specific topics, not necessarily because they are the best real-world design.</li>
  <li>The MySQL backend is included to meet course requirements and practice remote database interaction.</li>
</ul>

<h2>▶️ How to run</h2>

<ol>
  <li>Open a terminal in the project folder.</li>
  <li>Install dependencies if needed: <code>pip install pymysql</code>.</li>
  <li>Run the main script: <code>python main_sxed.py</code>.</li>
  <li>Follow the menu prompts to choose the database and perform operations.</li>
</ol>

<h2>📌 Notes for GitHub viewers</h2>

<ul>
  <li>This is a student exercise focused on practicing Python, database connectivity, and CRUD operations.</li>
  <li>The code uses a CLI approach because the assignment requested a command-line management system.</li>
  <li>If you are browsing this on GitHub, the main logic starts in <code>main_sxed.py</code> and uses the backend classes to perform database work.</li>
</ul>

<h2>🔧 Recommended setup for MySQL</h2>

<ul>
  <li>Install MySQL Server locally or use an existing server.</li>
  <li>Configure a database and user credentials before running the MySQL option.</li>
  <li>Update connection details in the project if needed to match your environment.</li>
</ul>

<p>If you want, I can also add a short setup example for the expected MySQL connection configuration.</p>
