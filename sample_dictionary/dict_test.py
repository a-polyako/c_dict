import random
import string
import shelve
import cProfile
import sample_dictionary

def set_dict(test_dict, random_max):
	for i in range(0, random_max):
		key = ''.join(random.choice(string.ascii_uppercase) for x in range(5))
		val = ''.join(random.choice(string.ascii_uppercase) for x in range(5))
		test_dict[key] = val
	print len(test_dict)
	return test_dict	

def get_dict(test_dict,random_max, keys):
	a = 0
	print len(keys)
	for key in keys:
		a = test_dict[key] 
def set_cdict(c_dict, keys, values, length):
        c_dict.populate(keys, values, length)
   

def get_cdict(c_dict, keys, length):
        c_dict.evacuate(keys, length)

def main():
	random_max = 100000
	test_dict = {}
	sdb = shelve.open('dict.db')
	if 'codes' in sdb:
		test_dict = sdb['codes']
		print len(test_dict)
	else:	
		print 'populating'
		cProfile.runctx('set_dict(test_dict, random_max)', globals(), locals())
		sdb['codes'] = test_dict
	sdb.close()
	print 'retrieving'
	keys = sorted(test_dict.keys())
	# get_dict(test_dict, random_max, keys)
	cProfile.runctx('get_dict(test_dict, random_max, keys)', globals(), locals())
	print 'done'
        c_dict = sample_dictionary.dict()
        print 'c dictionary created'
        (keys, values) = zip(*test_dict.items())
        keys = list(keys)
        values = list(values) 
        cProfile.runctx('set_cdict(c_dict, keys, values, len(keys))', globals(), locals())
        print 'c dictionary populated'
        cProfile.runctx('get_cdict(c_dict, keys, len(keys))', globals(), locals())
        print 'c dictionary retrived'

if __name__=='__main__':
	main()
