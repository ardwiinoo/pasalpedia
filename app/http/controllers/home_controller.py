from flask import render_template

class HomeController:
    def home():

        # dummy
        items = [
            {"data_applied": "Data 1", "status": "Active"},
            {"data_applied": "Data 2", "status": "Inactive"},
            {"data_applied": "Data 3", "status": "Pending"},
            {"data_applied": "Data 4", "status": "Completed"},
            {"data_applied": "Data 5", "status": "Reviewed"},
        ]

        return render_template('dashboard/home/index.html', items=items)