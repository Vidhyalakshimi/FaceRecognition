import cv2
import random

random.seed(10)
def generate_cropped_image_from_coordinates(img, major_axis_radius, center_x, center_y):
	ht = major_axis_radius
	x = center_x
	y = center_y

	min_x, min_y, max_x, max_y=max(x-ht,0), max(0,y-ht), x+ht, y+ht
	newimg = img[min_y:max_y,min_x:max_x]
	print min_x, min_y, max_x, max_y
	print "newimg[10,10]"
	print type(newimg)
	print newimg.shape
	resized_img = cv2.resize(newimg, (60, 60))
	print resized_img[10,10]
	return resized_img

def generate_cropped_faces(img, image_files):
	face_coords = image_files.readline().split(" ")
	major_axis_radius = int(round(float(face_coords[0])))
	center_x = int(round(float(face_coords[3])))
	center_y = int(round(float(face_coords[4])))
	new_img = generate_cropped_image_from_coordinates(img, major_axis_radius,center_x,center_y)
	print(major_axis_radius)
	print(center_y)
	print(center_x)
	return new_img

def generate_non_face(img):
	min_x = random.randint(0,60)
	min_y = random.randint(0,60)
 	return img[min_y:min_y+60, min_x:min_x+60]

def display_image(image):
	cv2.imshow('image', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
def extract_image(file_number, count):
	image_files = open("H:\NCSU\Courses\Sem2\CV\Project\FDDB-folds\FDDB-fold-0{}-ellipseList.txt".format(file_number))
	line = image_files.readline()
	while line:
		print line 
		# file = "H:\NCSU\Courses\Sem2\CV\Project\originalPics\{}.jpg".format(line.rstrip())
		file = "H:\NCSU\Courses\Sem2\CV\Project\originalPics\{}.jpg".format(line.rstrip())
		print file
		img=cv2.imread(file)
		print img[11,11]
		# display_image(img)
		#Fetch number of faces	
		number_of_faces = image_files.readline()
		if int(number_of_faces) == 1:	
			print file
			cropped_img = generate_cropped_faces(img, image_files) 
			non_face = generate_non_face(img)
			print(cropped_img[10,10])
			# saving cropped faces
			if count < 1050:
				cv2.imwrite("H:\NCSU\Courses\Sem2\CV\Project\Training\Positive\image{}.jpg".format(count), cropped_img)
				cv2.imwrite("H:\NCSU\Courses\Sem2\CV\Project\Training\Negative\image{}.jpg".format(count), non_face)
			elif count < 1150:
				cv2.imwrite("H:\NCSU\Courses\Sem2\CV\Project\Test\Positive\image{}.jpg".format(count), cropped_img)
				cv2.imwrite("H:\NCSU\Courses\Sem2\CV\Project\Test\Negative\image{}.jpg".format(count), non_face)
			count = count + 1
			# display_image(cropped_img)
		else:
			for i in range(1, int(number_of_faces)+1):
				temp = image_files.readline()
		print count
		if count > 1150:
			print "Thousand done"
			break
		line = image_files.readline()
		print(line)
	image_files.close()
	return count

count = 1
image_files = ""
for i in range(1, 10):
	count = extract_image(i, count)
	print "count"
	print count
	if(count > 1100):
		break