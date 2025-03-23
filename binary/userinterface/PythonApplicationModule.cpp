// 1) Search: search at the end 

}

// 2) before its end make a new line and paste:

#if defined(ENABLE_EXTENDED_SLIDERBAR)
	PyModule_AddIntConstant(poModule, "ENABLE_EXTENDED_SLIDERBAR", true);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_EXTENDED_SLIDERBAR", false);
#endif


// Example:

#if defined(ENABLE_EXTENDED_SLIDERBAR)
	PyModule_AddIntConstant(poModule, "ENABLE_EXTENDED_SLIDERBAR", true);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_EXTENDED_SLIDERBAR", false);
#endif

}