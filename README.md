# BonaClothiers
BonaClothiers is a fashion designer which produces top notch fashion from a variety of styles and colors for all customer demographics.

## Update: Version 0.6
Added several changes to frontend layout, several bug fixes, message system implemented for better alerts. See full update summary below;

* Fixed Style image not showing bug [ In edit styl section ]
* Fixed add inventory "form" does not exist error [ Typo: Spelt form INSTEAD of forms ]
* Disabled manager input field in the outfit section  [ To avoid the manager accidentally changing their username ]
* Changed the style  name input field to a select field
* Fixed edit styles section cancel button bug [ Was redirecting to all colors NOT all styles ]
  

## Update: Version 0.5
Added several changes to frontend layout, several bug fixes, message system implemented for better alerts. See full update summary below;

* Removed phonenumber from signup process
* Removed Date & Date Edited from all tables
* Added outfit style section [ Model, View, Template ] 
	* Add new outfit styles [ Styles name & Image ]
	* Edit/Update existing outfit styles
* Added proper alert system [ using django messages and discarding messages through url variables ]
* Changed name of table column [ Outfit Type -> Measurement Type & Product -> Outfit everywhere ]
* Fixed the image update bug [ was not updating because request.FILES was missing ]
* Added extra js [ responsible for image upload preview ]
* Added New form and model [ Transporter Information ]
	* Form was added to the delivery setting page
	* Transporter edit/delete view as well
* Moved add inventory -> all inventory section [ Both are one section now ]
* Added Modification views for all record categories [ Single views for delete and update for all records below each record view ]
* Added logout feature [ With proper alert system using django messages ]