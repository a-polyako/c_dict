#include <boost/unordered_map.hpp>
#include <boost/python.hpp>

typedef boost::unordered_map<std::string, std::string> map;

struct Dict{
	map m;
	void setValue(std::string key, std::string value)
	{
		m[key] = value;
	}
	std::string getValue(std::string key)
	{
		return m[key];
	}
	
	void populateDict(boost::python::list keys, boost::python::list values, int len)
	{
		for(int i = 0; i < len; i++)
		{
			m[boost::python::extract<std::string>(keys[i])] = boost::python::extract<std::string>(values[i]);
		}
	}
	
	void evacuateDict(boost::python::list keys, int len)
	{
		std::string a = "";
		for(int i = 0; i < len; i++)
		{
			a = m[boost::python::extract<std::string>(keys[i])];
		}
	}
			
};

using namespace boost::python;

BOOST_PYTHON_MODULE(sample_dictionary)
{
	class_<Dict>("dict")
		.def("set", &Dict::setValue)
		.def("get", &Dict::getValue)
		.def("populate", &Dict::populateDict)
		.def("evacuate", &Dict::evacuateDict)
	;

}

