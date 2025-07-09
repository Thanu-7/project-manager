from django.db import models

class Expense(models.Model):
    FOOD = 'Food'
    TRAVEL = 'Travel'
    BILLS = 'Bills'

    CATEGORY_CHOICES = [
        (FOOD, 'Food'),
        (TRAVEL, 'Travel'),
        (BILLS, 'Bills'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    expense_date = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.amount} ({self.category})"

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.status})"
