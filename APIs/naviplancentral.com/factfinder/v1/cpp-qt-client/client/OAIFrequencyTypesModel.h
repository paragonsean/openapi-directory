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
 * OAIFrequencyTypesModel.h
 *
 * 
 */

#ifndef OAIFrequencyTypesModel_H
#define OAIFrequencyTypesModel_H

#include <QJsonObject>

#include "OAIFrequencyTypeModel.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFrequencyTypeModel;

class OAIFrequencyTypesModel : public OAIObject {
public:
    OAIFrequencyTypesModel();
    OAIFrequencyTypesModel(QString json);
    ~OAIFrequencyTypesModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIFrequencyTypeModel> getFrequencyTypes() const;
    void setFrequencyTypes(const QList<OAIFrequencyTypeModel> &frequency_types);
    bool is_frequency_types_Set() const;
    bool is_frequency_types_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIFrequencyTypeModel> m_frequency_types;
    bool m_frequency_types_isSet;
    bool m_frequency_types_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFrequencyTypesModel)

#endif // OAIFrequencyTypesModel_H
