from django.db import models

# Create your models here.
class SparkData(models.Model):
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = "sparkdatastream"

"""
CREATE TABLE `sparkdatastream` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""