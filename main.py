import collector
import logger

logger.addSeparator('WINDOW=1')
collector.collect(1,0,1,0)
logger.addSeparator('WINDOW=2')
collector.collect(2,0,2,0)
logger.addSeparator('WINDOW=5')
collector.collect(5,0,5,0)

logger.addSeparator('WINDOW=10')
collector.collect(10,0,10,0)
logger.addSeparator('WINDOW=20')
collector.collect(20,0,20,0)
logger.addSeparator('WINDOW=50')
collector.collect(50,0,50,0)

logger.addSeparator('WINDOW=100')
collector.collect(100,0,100,0)
logger.addSeparator('WINDOW=200')
collector.collect(200,0,200,0)
logger.addSeparator('WINDOW=500')
collector.collect(500,0,500,0)

logger.addSeparator('WINDOW=1000')
collector.collect(1000,0,1000,0)
logger.addSeparator('End')
