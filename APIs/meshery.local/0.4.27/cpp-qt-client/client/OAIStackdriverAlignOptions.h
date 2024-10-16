/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIStackdriverAlignOptions.h
 *
 * StackdriverAlignOptions defines the list of alignment options shown in Grafana during query configuration.
 */

#ifndef OAIStackdriverAlignOptions_H
#define OAIStackdriverAlignOptions_H

#include <QJsonObject>

#include "OAIStackdriverAlignOption.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIStackdriverAlignOption;

class OAIStackdriverAlignOptions : public OAIObject {
public:
    OAIStackdriverAlignOptions();
    OAIStackdriverAlignOptions(QString json);
    ~OAIStackdriverAlignOptions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isExpanded() const;
    void setExpanded(const bool &expanded);
    bool is_expanded_Set() const;
    bool is_expanded_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    QList<OAIStackdriverAlignOption> getOptions() const;
    void setOptions(const QList<OAIStackdriverAlignOption> &options);
    bool is_options_Set() const;
    bool is_options_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_expanded;
    bool m_expanded_isSet;
    bool m_expanded_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    QList<OAIStackdriverAlignOption> m_options;
    bool m_options_isSet;
    bool m_options_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStackdriverAlignOptions)

#endif // OAIStackdriverAlignOptions_H
