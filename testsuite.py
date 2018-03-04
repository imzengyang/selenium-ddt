import unittest
import HTMLReport

from scenarios.register import Register

scenario_register = unittest.TestLoader().loadTestsFromTestCase(Register)
testsuite = unittest.TestSuite([scenario_register])


runner = HTMLReport.TestRunner(report_file_name='test',  
                               output_path='report',  
                               verbosity=2,  
                               title='测试报告',  
                               description='无测试描述',  
                               thread_count=1,  
                               
                               sequential_execution=True
                               
                               )

runner.run(testsuite)

