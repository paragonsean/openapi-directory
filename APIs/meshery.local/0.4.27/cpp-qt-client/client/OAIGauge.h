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
 * OAIGauge.h
 *
 * for a stat
 */

#ifndef OAIGauge_H
#define OAIGauge_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGauge : public OAIObject {
public:
    OAIGauge();
    OAIGauge(QString json);
    ~OAIGauge() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    float getMaxValue() const;
    void setMaxValue(const float &max_value);
    bool is_max_value_Set() const;
    bool is_max_value_Valid() const;

    float getMinValue() const;
    void setMinValue(const float &min_value);
    bool is_min_value_Set() const;
    bool is_min_value_Valid() const;

    bool isShow() const;
    void setShow(const bool &show);
    bool is_show_Set() const;
    bool is_show_Valid() const;

    bool isThresholdLabels() const;
    void setThresholdLabels(const bool &threshold_labels);
    bool is_threshold_labels_Set() const;
    bool is_threshold_labels_Valid() const;

    bool isThresholdMarkers() const;
    void setThresholdMarkers(const bool &threshold_markers);
    bool is_threshold_markers_Set() const;
    bool is_threshold_markers_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    float m_max_value;
    bool m_max_value_isSet;
    bool m_max_value_isValid;

    float m_min_value;
    bool m_min_value_isSet;
    bool m_min_value_isValid;

    bool m_show;
    bool m_show_isSet;
    bool m_show_isValid;

    bool m_threshold_labels;
    bool m_threshold_labels_isSet;
    bool m_threshold_labels_isValid;

    bool m_threshold_markers;
    bool m_threshold_markers_isSet;
    bool m_threshold_markers_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGauge)

#endif // OAIGauge_H
