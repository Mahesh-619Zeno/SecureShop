resource "aws_iam_policy" "bad_policy" {
  name        = "overly_permissive"
  description = "Bad example"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "s3:*"
        Resource = "arn:aws:s3:::*"
      },
      {
        Effect = "Allow"
        Action = ["iam:AttachRolePolicy"]
        Resource = "*"
      }
    ]
  })
}
