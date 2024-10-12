/**
 * Stationsdatenbereitstellung
 * An API providing master data for German railway stations by DB Station&Service AG.
 *
 * The version of the OpenAPI document: 2.2.01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIStation.h
 *
 * 
 */

#ifndef OAIStation_H
#define OAIStation_H

#include <QJsonObject>

#include "OAIAddress.h"
#include "OAIAufgabentraeger.h"
#include "OAIEVANumber.h"
#include "OAIPartial.h"
#include "OAIRegionalBereichRef.h"
#include "OAIRiL100Identifier.h"
#include "OAISZentraleRef.h"
#include "OAISchedule.h"
#include "OAIStationManagementRef.h"
#include "OAITimetableOffice.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISchedule;
class OAIAufgabentraeger;
class OAIEVANumber;
class OAIAddress;
class OAIRegionalBereichRef;
class OAIRiL100Identifier;
class OAIStationManagementRef;
class OAISZentraleRef;
class OAITimetableOffice;

class OAIStation : public OAIObject {
public:
    OAIStation();
    OAIStation(QString json);
    ~OAIStation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISchedule getDBinformation() const;
    void setDBinformation(const OAISchedule &d_binformation);
    bool is_d_binformation_Set() const;
    bool is_d_binformation_Valid() const;

    OAIAufgabentraeger getAufgabentraeger() const;
    void setAufgabentraeger(const OAIAufgabentraeger &aufgabentraeger);
    bool is_aufgabentraeger_Set() const;
    bool is_aufgabentraeger_Valid() const;

    qint32 getCategory() const;
    void setCategory(const qint32 &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QList<OAIEVANumber> getEvaNumbers() const;
    void setEvaNumbers(const QList<OAIEVANumber> &eva_numbers);
    bool is_eva_numbers_Set() const;
    bool is_eva_numbers_Valid() const;

    QString getFederalState() const;
    void setFederalState(const QString &federal_state);
    bool is_federal_state_Set() const;
    bool is_federal_state_Valid() const;

    bool isHasBicycleParking() const;
    void setHasBicycleParking(const bool &has_bicycle_parking);
    bool is_has_bicycle_parking_Set() const;
    bool is_has_bicycle_parking_Valid() const;

    bool isHasCarRental() const;
    void setHasCarRental(const bool &has_car_rental);
    bool is_has_car_rental_Set() const;
    bool is_has_car_rental_Valid() const;

    bool isHasDbLounge() const;
    void setHasDbLounge(const bool &has_db_lounge);
    bool is_has_db_lounge_Set() const;
    bool is_has_db_lounge_Valid() const;

    bool isHasLocalPublicTransport() const;
    void setHasLocalPublicTransport(const bool &has_local_public_transport);
    bool is_has_local_public_transport_Set() const;
    bool is_has_local_public_transport_Valid() const;

    bool isHasLockerSystem() const;
    void setHasLockerSystem(const bool &has_locker_system);
    bool is_has_locker_system_Set() const;
    bool is_has_locker_system_Valid() const;

    bool isHasLostAndFound() const;
    void setHasLostAndFound(const bool &has_lost_and_found);
    bool is_has_lost_and_found_Set() const;
    bool is_has_lost_and_found_Valid() const;

    QString getHasMobilityService() const;
    void setHasMobilityService(const QString &has_mobility_service);
    bool is_has_mobility_service_Set() const;
    bool is_has_mobility_service_Valid() const;

    bool isHasParking() const;
    void setHasParking(const bool &has_parking);
    bool is_has_parking_Set() const;
    bool is_has_parking_Valid() const;

    bool isHasPublicFacilities() const;
    void setHasPublicFacilities(const bool &has_public_facilities);
    bool is_has_public_facilities_Set() const;
    bool is_has_public_facilities_Valid() const;

    bool isHasRailwayMission() const;
    void setHasRailwayMission(const bool &has_railway_mission);
    bool is_has_railway_mission_Set() const;
    bool is_has_railway_mission_Valid() const;

    OAIPartial getHasSteplessAccess() const;
    void setHasSteplessAccess(const OAIPartial &has_stepless_access);
    bool is_has_stepless_access_Set() const;
    bool is_has_stepless_access_Valid() const;

    bool isHasTaxiRank() const;
    void setHasTaxiRank(const bool &has_taxi_rank);
    bool is_has_taxi_rank_Set() const;
    bool is_has_taxi_rank_Valid() const;

    bool isHasTravelCenter() const;
    void setHasTravelCenter(const bool &has_travel_center);
    bool is_has_travel_center_Set() const;
    bool is_has_travel_center_Valid() const;

    bool isHasTravelNecessities() const;
    void setHasTravelNecessities(const bool &has_travel_necessities);
    bool is_has_travel_necessities_Set() const;
    bool is_has_travel_necessities_Valid() const;

    bool isHasWiFi() const;
    void setHasWiFi(const bool &has_wi_fi);
    bool is_has_wi_fi_Set() const;
    bool is_has_wi_fi_Valid() const;

    OAISchedule getLocalServiceStaff() const;
    void setLocalServiceStaff(const OAISchedule &local_service_staff);
    bool is_local_service_staff_Set() const;
    bool is_local_service_staff_Valid() const;

    OAIAddress getMailingAdress() const;
    void setMailingAdress(const OAIAddress &mailing_adress);
    bool is_mailing_adress_Set() const;
    bool is_mailing_adress_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    qint32 getPriceCategory() const;
    void setPriceCategory(const qint32 &price_category);
    bool is_price_category_Set() const;
    bool is_price_category_Valid() const;

    OAIRegionalBereichRef getRegionalbereich() const;
    void setRegionalbereich(const OAIRegionalBereichRef &regionalbereich);
    bool is_regionalbereich_Set() const;
    bool is_regionalbereich_Valid() const;

    QList<OAIRiL100Identifier> getRiL100Identifiers() const;
    void setRiL100Identifiers(const QList<OAIRiL100Identifier> &ri_l100_identifiers);
    bool is_ri_l100_identifiers_Set() const;
    bool is_ri_l100_identifiers_Valid() const;

    OAIStationManagementRef getStationManagement() const;
    void setStationManagement(const OAIStationManagementRef &station_management);
    bool is_station_management_Set() const;
    bool is_station_management_Valid() const;

    OAISZentraleRef getSzentrale() const;
    void setSzentrale(const OAISZentraleRef &szentrale);
    bool is_szentrale_Set() const;
    bool is_szentrale_Valid() const;

    OAITimetableOffice getTimetableOffice() const;
    void setTimetableOffice(const OAITimetableOffice &timetable_office);
    bool is_timetable_office_Set() const;
    bool is_timetable_office_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISchedule m_d_binformation;
    bool m_d_binformation_isSet;
    bool m_d_binformation_isValid;

    OAIAufgabentraeger m_aufgabentraeger;
    bool m_aufgabentraeger_isSet;
    bool m_aufgabentraeger_isValid;

    qint32 m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QList<OAIEVANumber> m_eva_numbers;
    bool m_eva_numbers_isSet;
    bool m_eva_numbers_isValid;

    QString m_federal_state;
    bool m_federal_state_isSet;
    bool m_federal_state_isValid;

    bool m_has_bicycle_parking;
    bool m_has_bicycle_parking_isSet;
    bool m_has_bicycle_parking_isValid;

    bool m_has_car_rental;
    bool m_has_car_rental_isSet;
    bool m_has_car_rental_isValid;

    bool m_has_db_lounge;
    bool m_has_db_lounge_isSet;
    bool m_has_db_lounge_isValid;

    bool m_has_local_public_transport;
    bool m_has_local_public_transport_isSet;
    bool m_has_local_public_transport_isValid;

    bool m_has_locker_system;
    bool m_has_locker_system_isSet;
    bool m_has_locker_system_isValid;

    bool m_has_lost_and_found;
    bool m_has_lost_and_found_isSet;
    bool m_has_lost_and_found_isValid;

    QString m_has_mobility_service;
    bool m_has_mobility_service_isSet;
    bool m_has_mobility_service_isValid;

    bool m_has_parking;
    bool m_has_parking_isSet;
    bool m_has_parking_isValid;

    bool m_has_public_facilities;
    bool m_has_public_facilities_isSet;
    bool m_has_public_facilities_isValid;

    bool m_has_railway_mission;
    bool m_has_railway_mission_isSet;
    bool m_has_railway_mission_isValid;

    OAIPartial m_has_stepless_access;
    bool m_has_stepless_access_isSet;
    bool m_has_stepless_access_isValid;

    bool m_has_taxi_rank;
    bool m_has_taxi_rank_isSet;
    bool m_has_taxi_rank_isValid;

    bool m_has_travel_center;
    bool m_has_travel_center_isSet;
    bool m_has_travel_center_isValid;

    bool m_has_travel_necessities;
    bool m_has_travel_necessities_isSet;
    bool m_has_travel_necessities_isValid;

    bool m_has_wi_fi;
    bool m_has_wi_fi_isSet;
    bool m_has_wi_fi_isValid;

    OAISchedule m_local_service_staff;
    bool m_local_service_staff_isSet;
    bool m_local_service_staff_isValid;

    OAIAddress m_mailing_adress;
    bool m_mailing_adress_isSet;
    bool m_mailing_adress_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    qint32 m_price_category;
    bool m_price_category_isSet;
    bool m_price_category_isValid;

    OAIRegionalBereichRef m_regionalbereich;
    bool m_regionalbereich_isSet;
    bool m_regionalbereich_isValid;

    QList<OAIRiL100Identifier> m_ri_l100_identifiers;
    bool m_ri_l100_identifiers_isSet;
    bool m_ri_l100_identifiers_isValid;

    OAIStationManagementRef m_station_management;
    bool m_station_management_isSet;
    bool m_station_management_isValid;

    OAISZentraleRef m_szentrale;
    bool m_szentrale_isSet;
    bool m_szentrale_isValid;

    OAITimetableOffice m_timetable_office;
    bool m_timetable_office_isSet;
    bool m_timetable_office_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStation)

#endif // OAIStation_H
