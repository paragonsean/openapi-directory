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
 * OAIFactFinderModuleModel.h
 *
 * 
 */

#ifndef OAIFactFinderModuleModel_H
#define OAIFactFinderModuleModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFactFinderModuleModel : public OAIObject {
public:
    OAIFactFinderModuleModel();
    OAIFactFinderModuleModel(QString json);
    ~OAIFactFinderModuleModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAvailable() const;
    void setAvailable(const bool &available);
    bool is_available_Set() const;
    bool is_available_Valid() const;

    QString getModuleName() const;
    void setModuleName(const QString &module_name);
    bool is_module_name_Set() const;
    bool is_module_name_Valid() const;

    bool isVisited() const;
    void setVisited(const bool &visited);
    bool is_visited_Set() const;
    bool is_visited_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_available;
    bool m_available_isSet;
    bool m_available_isValid;

    QString m_module_name;
    bool m_module_name_isSet;
    bool m_module_name_isValid;

    bool m_visited;
    bool m_visited_isSet;
    bool m_visited_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFactFinderModuleModel)

#endif // OAIFactFinderModuleModel_H
