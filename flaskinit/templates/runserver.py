from {{ project }}.wsgi import app


if __name__ == '__main__':
  app.run(debug=True)