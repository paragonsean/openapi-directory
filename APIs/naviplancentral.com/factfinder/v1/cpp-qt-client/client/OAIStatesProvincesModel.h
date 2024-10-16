/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIStatesProvincesModel.h
 *
 * 
 */

#ifndef OAIStatesProvincesModel_H
#define OAIStatesProvincesModel_H

#include <QJsonObject>

#include "OAIStateProvinceModel.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIStateProvinceModel;

class OAIStatesProvincesModel : public OAIObject {
public:
    OAIStatesProvincesModel();
    OAIStatesProvincesModel(QString json);
    ~OAIStatesProvincesModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIStateProvinceModel> getStatesProvinces() const;
    void setStatesProvinces(const QList<OAIStateProvinceModel> &states_provinces);
    bool is_states_provinces_Set() const;
    bool is_states_provinces_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIStateProvinceModel> m_states_provinces;
    bool m_states_provinces_isSet;
    bool m_states_provinces_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStatesProvincesModel)

#endif // OAIStatesProvincesModel_H
