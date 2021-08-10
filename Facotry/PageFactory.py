from Dashboard import Dashboards



def PageObject(page_name, driver):

	test_obj = None
	if page_name == "Dashboard":
		test_obj = Dashboards(driver)
	return test_obj