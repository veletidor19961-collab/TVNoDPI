package io.github.romanvht.byedpi.fragments

import android.content.Intent
import android.os.Bundle
import androidx.preference.Preference
import androidx.preference.PreferenceFragmentCompat
import io.github.romanvht.byedpi.R
import io.github.romanvht.byedpi.activities.SettingsActivity
import io.github.romanvht.byedpi.activities.TestActivity
import io.github.romanvht.byedpi.activities.TestSettingsActivity

class MainSettingsFragment : PreferenceFragmentCompat() {
    override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
        setPreferencesFromResource(R.xml.main_settings, rootKey)

        findPreference<Preference>("tv_strategy_editor")?.setOnPreferenceClickListener {
            parentFragmentManager
                .beginTransaction()
                .replace(R.id.settings, ByeDpiCMDSettingsFragment())
                .addToBackStack(null)
                .commit()
            true
        }

        findPreference<Preference>("tv_strategy_test")?.setOnPreferenceClickListener {
            startActivity(Intent(requireContext(), TestActivity::class.java))
            true
        }

        findPreference<Preference>("tv_domain_lists")?.setOnPreferenceClickListener {
            val intent = Intent(requireContext(), TestSettingsActivity::class.java)
            intent.putExtra("open_fragment", "domain_lists")
            startActivity(intent)
            true
        }
    }
}
