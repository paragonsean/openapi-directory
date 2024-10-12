QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIHoliday.h \
    $${PWD}/OAIHoliday_200_response.h \
    $${PWD}/OAIHoliday_400_response.h \
    $${PWD}/OAIHolidays_200_response.h \
    $${PWD}/OAIProvince.h \
    $${PWD}/OAIProvince_200_response.h \
    $${PWD}/OAIProvinces_200_response.h \
    $${PWD}/OAIRoot_200_response.h \
    $${PWD}/OAIRoot_200_response__links.h \
    $${PWD}/OAIRoot_200_response__links_holidays.h \
    $${PWD}/OAIRoot_200_response__links_provinces.h \
    $${PWD}/OAIRoot_200_response__links_self.h \
    $${PWD}/OAIRoot_200_response__links_spec.h \
# APIs
    $${PWD}/OAIHolidaysApi.h \
    $${PWD}/OAIInfoApi.h \
    $${PWD}/OAIProvincesApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIHoliday.cpp \
    $${PWD}/OAIHoliday_200_response.cpp \
    $${PWD}/OAIHoliday_400_response.cpp \
    $${PWD}/OAIHolidays_200_response.cpp \
    $${PWD}/OAIProvince.cpp \
    $${PWD}/OAIProvince_200_response.cpp \
    $${PWD}/OAIProvinces_200_response.cpp \
    $${PWD}/OAIRoot_200_response.cpp \
    $${PWD}/OAIRoot_200_response__links.cpp \
    $${PWD}/OAIRoot_200_response__links_holidays.cpp \
    $${PWD}/OAIRoot_200_response__links_provinces.cpp \
    $${PWD}/OAIRoot_200_response__links_self.cpp \
    $${PWD}/OAIRoot_200_response__links_spec.cpp \
# APIs
    $${PWD}/OAIHolidaysApi.cpp \
    $${PWD}/OAIInfoApi.cpp \
    $${PWD}/OAIProvincesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
